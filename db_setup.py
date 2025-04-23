from app.domain       import *
from app              import create_app
from app.extensions   import db

app = create_app()

def create_tables():
    with app.app_context():
        db.create_all()
        print("✅ Tables created.")


# ─── 4. Seed initial data ────────────────────────────────────────────────────
def seed_data():
    """Populate your tables with some starter data. Customize as needed."""
    with app.app_context():
        # — Example: Create companies
        cleaning_master = Company(
            name='CleaningMaster Corp',
            address='123 Main St',
            phone='555-0100',
            email='info@example.com',
            logo_url=None
        )
        db.session.add(cleaning_master)

        eco_clean = Company(
            name='EcoClean Solutions',
            address='456 Other St',
            phone='666-0200',
            email='eco@email.com',
            logo_url=None
        )
        db.session.add(eco_clean)

        clean_guys = Company(
            name='Clean Guys',
            address='789 Guys St',
            phone='777-0300',
            email='guys@email.com',
            logo_url=None
        )
        db.session.add(clean_guys)

        # — Example: Create a user (adjust keyword args to match your User.__init__)
        user = User(
            username='davizacheu',
            password='davi1234',
            email="davi@email.com"
        )
        db.session.add(user)

        # — Example: Create roles
        administrator = Role(
            role_title='Administrator',
        )
        cleaning_master.roles.append(administrator)
        user.roles.append(administrator)
        supervisor = Role(
            role_title='Supervisor',
        )
        eco_clean.roles.append(supervisor)
        user.roles.append(supervisor)

        # — Example: Create orders
        mall = Order(
            name='Mall Office',
            description='Clean the mall office',
            created_at='2021-01-01',
        )
        apt = Order(
            name='Apartment',
            description='Clean the apartment',
            created_at='2021-01-01',
        )
        clean_guys.orders.append(mall)
        user.orders.append(mall)
        user.orders.append(apt)

        # Commit all seeded objects
        db.session.commit()
        print("✅ Seed data inserted.")


# ─── 5. Entrypoint ────────────────────────────────────────────────────────────
if __name__ == '__main__':
    create_tables()
    seed_data()
    print("🎉 Done.")
