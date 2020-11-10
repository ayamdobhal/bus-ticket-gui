def table_check(CURSOR):
    CURSOR.execute("select * from information_schema.tables where table_name = 'admin';")
    if CURSOR.fetchone()[0] == 1:
        return True
    return False

def create_tables(CURSOR):
    try:
        CURSOR.execute('''create table admin(
                    username varchar(255) primary key,
                    password varchar(255) not null);'''
                )
        CURSOR.execute('''create table buses(
                    bus_id int(10) primary key,
                    bus_name varchar(255) not null);'''
                )
        CURSOR.execute('''create table tkt_status(
                    tkt_no int(20) primary key,
                    status varchar(255));'''
                )
        CURSOR.execute('''create table traveller(
                    trvlr_id int(16) primary key,
                    trvlr_fname varchar(255) not null,
                    trvlr_lname varchar(255),
                    trvlr_age int(2),
                    trvlr_email varchar(255),
                    trvlr_phone int(10));'''
                )
        CURSOR.execute('''create table payment(
                    seat_number int(3),
                    meal varchar(6),
                    baggage varchar(255),
                    tkt_no int(20),
                    trvlr_id int(16));'''
                )
        CURSOR.execute('''create table ticket(
                    tkt_no int(2) primary key,
                    coupon_code varchar(10),
                    net_price int(6),
                    price int(6));'''
                )
        CURSOR.execute('''create table booking(
                    no_of_psngr int(3),
                    pay_in int(6),
                    dep_frm varchar(255),
                    dep_date date,
                    ret_date date,
                    destination varchar(255));'''
                )
        CURSOR.execute('''create table customer(
                    username varchar(255) primary key,
                    password varchar(24) not null,
                    email varchar(255) not null,
                    age int(2) not null,
                    fname varchar(255),
                    lname varchar(255),
                    phone int(10) not null);'''
                )
        CONNECTION.commit()
        print('database created succesfully!')
    except:
        print('Error')
