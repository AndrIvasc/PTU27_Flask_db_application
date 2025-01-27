from models import Projektas, db
from app import app

with app.app_context():
    projects =  [
        Projektas(pavadinimas="Rojaus sodai", kaina=50000.7),
        Projektas(pavadinimas="Maxima", kaina=1000000.0),
        Projektas(pavadinimas="Kavaliauskas-Gronskis", kaina=270.0),
        Projektas(pavadinimas="Grinius Ltd", kaina=770.0),
        Projektas(pavadinimas="Žukauskas-Vsiliauskas", kaina=880.0),
        Projektas(pavadinimas="Poška-Nausėda", kaina=775.0),
        Projektas(pavadinimas="Kalvaitis Ltd", kaina=905.0),
        Projektas(pavadinimas="Gaižauskas-Gailys", kaina=1010.0),
        Projektas(pavadinimas="Poška and Sons", kaina=275.0),
        Projektas(pavadinimas="Akelis, Kairys and Kalvelis", kaina=815.0),
        Projektas(pavadinimas="Urbonas Inc", kaina=835.0),
        Projektas(pavadinimas="Paulauskas-Gaižauskas", kaina=380.0),
        Projektas(pavadinimas="Butkus-Stankevičius", kaina=405.0),
        Projektas(pavadinimas="Gailys, Gronskis and Gaičiūnas", kaina=145.0),
        Projektas(pavadinimas="Poška and Sons", kaina=610.0),
        Projektas(pavadinimas="Stankevičius Group", kaina=575.0),
        Projektas(pavadinimas="Kazlauskas PLC", kaina=1095.0),
        Projektas(pavadinimas="Sakalauskas-Povilonis", kaina=260.0),
        Projektas(pavadinimas="Stankevičius PLC", kaina=965.0),
        Projektas(pavadinimas="Butkus, Ambrasas and Gaižauskas", kaina=960.0),
        Projektas(pavadinimas="Gagys, Vsiliauskas and Kavaliauskas", kaina=730.0),
        Projektas(pavadinimas="Kairys, Kiška and Gailius", kaina=1075.0),
        Projektas(pavadinimas="Galdikas, Kalvaitis and Kavaliauskas", kaina=120.0),
        Projektas(pavadinimas="Gailys Inc", kaina=835.0),
        Projektas(pavadinimas="Gailius-Povilonis", kaina=800.0),
        Projektas(pavadinimas="Povilonis Inc", kaina=130.0),
        Projektas(pavadinimas="Galdikas, Kalvėnas and Kavaliauskas", kaina=1010.0),
        Projektas(pavadinimas="Kalvaitis-Kavaliauskas", kaina=985.0),
        Projektas(pavadinimas="Jankauskas, Paulauskas and Kiška", kaina=110.0),
        Projektas(pavadinimas="Narušis, Paulauskas and Stankevičius", kaina=1020.0),
        Projektas(pavadinimas="Sons and Akelis Inc.", kaina=790.5)
    ]

    db.session.add_all(projects)
    db.session.commit()
    print("Duomenis uzpildyti")


