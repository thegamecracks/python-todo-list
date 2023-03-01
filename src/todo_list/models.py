from sqlalchemy import ForeignKey, String, Uuid
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    mapped_column,
    relationship,
)

__all__ = (
    "Base",
    "User",
    "TodoEntry",
)


class Base(MappedAsDataclass, DeclarativeBase, kw_only=True):
    ...


class User(Base, kw_only=True):
    __tablename__ = "user_account"

    user_id: Mapped[Uuid] = mapped_column(Uuid, init=False, primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    todo_entries: Mapped[list["TodoEntry"]] = relationship(
        back_populates="user",
        default_factory=list,
    )


class TodoEntry(Base, kw_only=True):
    __tablename__ = "todo_entry"

    entry_id: Mapped[Uuid] = mapped_column(Uuid, init=False, primary_key=True)

    user_id: Mapped[Uuid] = mapped_column(
        ForeignKey("user_account.user_id"),
        init=False,
    )

    user: Mapped[User] = relationship(
        back_populates="todo_entries",
        default=None,
    )


if __name__ == "__main__":
    from sqlalchemy import create_mock_engine

    def dump(sql, *multiparams, **params):
        print(sql.compile(dialect=engine.dialect))

    engine = create_mock_engine(
        "postgresql+psycopg2://",  # type: ignore
        dump,
    )
    Base.metadata.create_all(engine)
