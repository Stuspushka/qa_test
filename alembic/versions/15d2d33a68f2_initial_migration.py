"""create questions and answers tables

Revision ID: e6b7f990ae0f
Revises:
Create Date: 2025-11-15 16:29:35.059281
"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa

revision = 'e6b7f990ae0f'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        "questions",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("text", sa.Text, nullable=False),
        sa.Column("created_at", sa.DateTime, default=datetime.utcnow, nullable=False),
    )

    op.create_table(
        "answers",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("question_id", sa.Integer, sa.ForeignKey("questions.id", ondelete="CASCADE"), nullable=False),
        sa.Column("user_id", sa.String, nullable=False),
        sa.Column("text", sa.Text, nullable=False),
        sa.Column("created_at", sa.DateTime, default=datetime.utcnow, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("answers")
    op.drop_table("questions")
