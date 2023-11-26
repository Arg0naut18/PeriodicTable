# Periodic Table

### To run API locally
- Make sure you have docker locally installed.
- Contact me to get you added to the MongoDB as a user of the database.
- Run `docker build --build-arg mongo_username=<mongo username> --build-arg mongo_password=<mongo password> -t periodic-table .`
- Run `docker run -d -p 80:80 --name PeriodicTableAPI periodic-table`