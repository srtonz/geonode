#!/usr/bin/env bash

set -x

if [ "$BACKEND" = "geonode.geoserver" ]; then

	case $1 in
		"before_install")
			echo "Before install scripts"
			;;
		"before_script")
			echo "Setting up PostGIS Backend"
			export GEONODE_PROJECT_PATH=$TRAVIS_BUILD_DIR
      sudo -u postgres dropdb -h 127.0.0.1 -u runner template_postgis
      sudo -u postgres dropdb -h 127.0.0.1 -u runner geonode
      sudo -u postgres dropdb -h 127.0.0.1 -u runner geonode_data
      sudo -u postgres dropdb -h 127.0.0.1 -u runner upload_test
      sudo -u postgres dropdb -h 127.0.0.1 -u runner test_upload_test
      sudo -u postgres dropuser -h 127.0.0.1 -u runner geonode
      sudo -u postgres createuser -h 127.0.0.1 -u runner geonode -d -s
      sudo -u postgres psql --h 127.0.0.1 -u runner c "ALTER USER geonode WITH PASSWORD 'geonode';"
      sudo -u postgres createdb -h 127.0.0.1 -u runner template_postgis
      sudo -u postgres psql --h 127.0.0.1 -u runner d template_postgis -c 'CREATE EXTENSION postgis;'
      sudo -u postgres psql --h 127.0.0.1 -u runner d template_postgis -c 'GRANT ALL ON geometry_columns TO PUBLIC;'
      sudo -u postgres psql --h 127.0.0.1 -u runner d template_postgis -c 'GRANT ALL ON spatial_ref_sys TO PUBLIC;'
      sudo -u postgres psql --h 127.0.0.1 -u runner d template_postgis -c 'GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO geonode;'
      sudo -u postgres createdb --h 127.0.0.1 -u runner O geonode geonode
      sudo -u postgres createdb --h 127.0.0.1 -u runner T template_postgis -O geonode geonode_data
      sudo -u postgres createdb --h 127.0.0.1 -u runner T template_postgis -O geonode upload_test
			;;
		"after_script")
			;;
	esac
fi
