"""
scripts/clear_data.py

Script para esvaziar todas as tabelas do banco (mantendo o esquema).
- Exclui todas as linhas de todas as tabelas (exceto `alembic_version`).
- Roda VACUUM se o banco for SQLite para compactar o arquivo.

Uso:
  # pedir confirmação interativa
  poetry run python scripts/clear_data.py

  # sem confirmação (útil em CI):
  poetry run python scripts/clear_data.py --yes

AVISO: faça backup antes se houver dados importantes!
"""

import argparse
import sys

from sqlalchemy import inspect, text

from fastapi_zero.databse import engine


def clear_all_tables(dry_run: bool = False):
    inspector = inspect(engine)
    tables = [t for t in inspector.get_table_names() if t != 'alembic_version']

    if not tables:
        print('Nenhuma tabela encontrada.')
        return

    with engine.begin() as conn:
        for t in tables:
            print(f"Apagando tabela '{t}'...")
            if not dry_run:
                conn.execute(text(f'DELETE FROM "{t}";'))

    # Se for SQLite, compacta o arquivo
    try:
        if engine.url.drivername.startswith('sqlite'):
            with engine.connect() as conn:
                conn.exec_driver_sql('VACUUM;')
    except Exception as exc:
        print('VACUUM falhou:', exc)

    print('Concluído: tabelas esvaziadas (esquema mantido).')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Esvaziar todas as tabelas (preserva esquema)'
    )
    parser.add_argument(
        '--yes',
        '-y',
        action='store_true',
        help='Ignora confirmação interativa',
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Mostra o que seria apagado sem executar',
    )
    args = parser.parse_args()

    if not args.yes:
        resp = input(
            'Tem certeza que deseja esvaziar todas as tabelas? [y/N] '
        )
        if resp.lower() != 'y':
            print('Cancelado pelo usuário.')
            sys.exit(0)

    clear_all_tables(dry_run=args.dry_run)
