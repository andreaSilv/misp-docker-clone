This repository is born to keep all changes I'm doing on [original docker image](https://github.com/harvard-itsecurity/docker-misp).

# How to run

Please follow steps below:

1. Initialize database
   ```bash
   docker run -it --rm \
      -v /docker/misp:/var/lib/mysql \
      harvarditsecurity/misp /init-db
   ```

2. Build container
   Go with Ubuntu terminal in this repository and run - THIS COULD TAKE UP TO 20 MINS
   ```bash
   ./build.sh
   ```
   Build command will tag your container `harvarditsecurity/misp:latest`

3. Run the container
   ```bash
   docker run -it --rm \
      -p 8080:8080 \
      -p 3306:3306 \
      -p 6666:6666 \
      -v /docker/misp:/var/lib/mysql \
      harvarditsecurity/misp:latest
   ```

4. Open the ui from your browser [https://localhost:8443](https://localhost:8443)
   - Default credential:
     - **Email**: `admin@admin.test`
     - **Password**: `admin`
   
     New example password `Password1234`


I'm writing journey notes [here](./notes/NOTES.md)