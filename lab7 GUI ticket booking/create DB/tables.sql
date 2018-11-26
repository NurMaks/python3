create table Users (
	id SERIAL PRIMARY KEY,
	login varchar(20) not null unique,
	password varchar(50) not null,
	name varchar(20) not null,
	surname varchar(20) not null
);

create table Tickets (
	id SERIAL PRIMARY KEY,
	user_id integer references Users(id),
	cinema text not null,
	film text not null,
	time text not null,
	place text not null,
	price real not null,
	totalPrice real not null
);

create table Cinemas (
	id SERIAL PRIMARY KEY,
	name text not null unique
);

create table Films (
	id SERIAL PRIMARY KEY,
	name text not null unique
);

create table Times (
	id SERIAL PRIMARY KEY,
	cinema_id integer references Cinemas(id),
	film_id integer references Films(id),
	time text not null,
	price real not null
);

create table Halls (
	id SERIAL PRIMARY KEY,
	time_id integer references Times(id),
	place integer not null,
	status integer not null
);