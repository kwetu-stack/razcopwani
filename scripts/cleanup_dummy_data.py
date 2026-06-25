from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from app import create_app
from models import LostAccount, Visit, Opportunity, ActionPlan, db

app = create_app()

with app.app_context():

    print("Before Cleanup")
    print("Lost:", LostAccount.query.count())
    print("Visits:", Visit.query.count())
    print("Opps:", Opportunity.query.count())
    print("Plans:", ActionPlan.query.count())

    LostAccount.query.delete()
    Visit.query.delete()
    Opportunity.query.delete()
    ActionPlan.query.delete()

    db.session.commit()

    print("\nAfter Cleanup")
    print("Lost:", LostAccount.query.count())
    print("Visits:", Visit.query.count())
    print("Opps:", Opportunity.query.count())
    print("Plans:", ActionPlan.query.count())