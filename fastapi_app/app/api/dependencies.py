import os
from pathlib import Path

from sqlalchemy.orm import Session

from db.session import get_sessionmaker

BASE_DIR = Path(__file__).resolve().parent.parent


def read_boolean(value: str) -> bool:
    """
    文字列をbool型に変換する。
    環境変数を読み込むときに使用する。

    Parameters
    ----------
    value : str
        環境変数のDEBUG変数として設定されている値。

    Returns
    -------
    bool
        Trueに相当する値ならTrue，Falseに相当する値ならFalse。
    """
    return value.lower() in ('true', 't', 'yes', 'y', 'on', '1')


def get_session(dotenv_path: str) -> Session:
    SessionLocal = get_sessionmaker(dotenv_path)
    return SessionLocal()


async def get_session_prod():
    session = get_session(BASE_DIR / "postgres" / ".env")
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()


async def get_session_dev():
    session = get_session(BASE_DIR / "postgres" / ".env.dev")
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()
