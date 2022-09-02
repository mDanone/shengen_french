from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import backref, declarative_base, relationship

# declarative base class
Base = declarative_base()

# an example mapping using the base
class TelegramUser(Base):
    __tablename__ = 'telegram_user'

    id = Column(Integer, primary_key=True)


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)


class TaskCategory(Base):
    __tablename__ = "task_categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    subcategories = relationship(
        "SubCategory",
        backref=backref("task_category", lazy="selectin"),
        lazy="selectin",
        cascade="all, delete",
    )


class SubCategory(Base):
    __tablename__ = "sub_categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    task_category_id = Column(Integer, ForeignKey("task_categories.id", ondelete="CASCADE"))