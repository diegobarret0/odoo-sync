from sqlalchemy import Column, Integer, String, UniqueConstraint
from db.session import Base

class SyncLink(Base):
    __tablename__ = "sync_link"

    id = Column(Integer, primary_key=True, index=True)
    origin = Column(String, nullable=False)
    origin_model = Column(String, nullable=False)
    origin_id = Column(Integer, nullable=False)
    destiny = Column(String, nullable=False)
    destiny_model = Column(String, nullable=False)
    destiny_id = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint('origin', 'origin_model', 'origin_id', 'destiny', 'destiny_model'),
    )
