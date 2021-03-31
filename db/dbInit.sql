create database if not exists CC_T3;

use CC_T3;

drop table if exists Hospital_Admission;
drop table if exists Hospital_Opinion;
drop table if exists Hospital;
drop table if exists Vaccination_Appointment;
drop table if exists Vaccination_Centre;
drop table if exists Vaccine_Type;
drop table if exists News;

create or replace table Hospital (
    ID integer primary key  auto_increment,
    name varchar(256) not null,
    address varchar(256) not null,

    constraint unique (name, address)
);

create or replace  table Hospital_Opinion (
    ID integer primary key auto_increment,

    title varchar(64) not null unique ,
    message varchar(512) not null,

    hospital_ID integer not null,

    constraint foreign key hospital_opinion_valid_h_ID(hospital_ID) references
                              Hospital(ID) on delete cascade
);

create or replace  table Hospital_Admission (
    ID integer primary key auto_increment,

    admitted integer default 0,
    vaccinated integer default 0,

    hospital_ID integer not null,

    entry_date datetime default sysdate(),

    constraint unique (hospital_ID, entry_date),

    constraint foreign key hospital_admission_valid_h_ID(hospital_ID) references
                                 Hospital(ID) on delete cascade
);

create or replace  table Vaccine_Type (
    ID integer primary key  not null auto_increment,
    name varchar(64) unique not null
);

insert into Vaccine_Type (name) values
('Astra-Zenneca'), ('Pfizer'), ('Moderna');


create or replace  table Vaccination_Centre (
    ID integer primary key auto_increment,

    address varchar(256) not null unique,
    dose_count integer not null,

    dose_type_ID integer not null,

    constraint foreign key dose_type_valid_ID (dose_type_ID) references
                                Vaccine_Type(ID) on delete cascade
);

create or replace  table Vaccination_Appointment (
    ID integer primary key auto_increment,

    person_name varchar(128) unique not null ,
    app_date datetime not null,

    vacc_centre_ID integer not null,

    constraint foreign key vacc_centre_valid_vc_ID (vacc_centre_ID) references
                                     Vaccination_Centre(ID) on delete cascade
);


create or replace  table News (
    ID integer primary key auto_increment,

    title varchar(128) unique not null,
    content text(16384) not null
);