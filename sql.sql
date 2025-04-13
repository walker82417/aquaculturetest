CREATE TABLE aquaculture_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    ph_level REAL,
    temperature REAL,
    turbidity REAL,
    flow_rate REAL,
    water_level REAL
);

select * from aquaculture_data;