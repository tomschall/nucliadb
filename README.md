# NucliaDB Example

## Quick start

`Build image and start container`

```
docker build -t nucliadb .
docker run --name nucliadb -p 8080:8080 nucliadb
```

`Connect to container`

```
docker exec -ti nucliadb bash
```

`Pushing data to nucliadb`

```
python3 ploneconf_upload_oss.py
```

`Now you can search your knowledge box`

[http://0.0.0.0:8080/widget/](http://0.0.0.0:8080/widget/)

`Query data over python script`

```
python3 ploneconf_query_oss.py
```
