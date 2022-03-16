CREATE SCHEMA IF NOT EXISTS snapshots;

CREATE SCHEMA IF NOT EXISTS hass_schema;

DROP TABLE IF EXISTS hass_schema.states;

CREATE TABLE hass_schema.states (
	state_id int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	"domain" varchar(64) NULL,
	entity_id varchar(255) NULL,
	state varchar(255) NULL,
	"attributes" text NULL,
	event_id int4 NULL,
	last_changed timestamptz NULL,
	last_updated timestamptz NULL,
	created timestamptz NULL,
	old_state_id int4 NULL,
	CONSTRAINT states_pkey PRIMARY KEY (state_id)
);
CREATE INDEX ix_states_entity_id_last_updated ON hass_schema.states USING btree (entity_id, last_updated);
CREATE INDEX ix_states_event_id ON hass_schema.states USING btree (event_id);
CREATE INDEX ix_states_last_updated ON hass_schema.states USING btree (last_updated);
CREATE INDEX ix_states_old_state_id ON hass_schema.states USING btree (old_state_id);

COPY hass_schema.states (state_id,domain,entity_id,state,attributes,event_id,last_changed,last_updated,created,old_state_id)
FROM '/input_data/states.csv' DELIMITER ',' CSV HEADER;

