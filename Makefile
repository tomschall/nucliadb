clear-oss:
	rm -rf blob
	rm -rf main
	rm -rf node

clear-cloud:
	rm -rf blobnuclia
	rm -rf mainnuclia
	rm -rf nodenuclia

nucliadb-cloud:
	nucliadb  --zone europe-1 --maindb mainnuclia --blob blobnuclia --node nodenuclia --log INFO  --key eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6InNhIn0.eyJpc3MiOiJodHRwczovL251Y2xpYS5jbG91ZC8iLCJleHAiOjE2OTcyOTUwNjgsImlhdCI6MTY2NTc1OTA2OCwic3ViIjoiNzIwMGU5ZTYtNGQ3OS00OTc3LWI3MmQtZGQ2Njg1YmZiMWQ3IiwianRpIjoiN2NmZjFmODUtZDhjMy00OGQzLWIzM2YtNTgwNDBmOWZmZGNkIiwia2V5IjoiM2Y3OGUzM2ItNDU0Mi00NWYzLWE2MzctZTZiM2NkN2NmNGY4Iiwia2lkIjoiMWIzZTJhNjQtODJlMS00MWM5LWI1M2ItZWY5NzI0ZTc5NjE4In0.I0kamdtjJkgc8xKFhuFB2I-Uwdh7uJ7MR1aq85vdFX3ll9ewnicAWOwUtsUt37E_juSIWzNrmQq2vlbqqljY-JNO2x4oyqZ1qN-UBYL20nsuI7oqKIZBol_QoKmOUHTCm1ciwNTwckUiudZ3usT2OKNAmEe4pIAQnq57dc_6vj79kG35kb_8J6aqWm0zRj9u_EJCjEB72foK-njjk0QVBDhyTxGbXjdAqdztAq9Ry50ZtkMkgl5_sau5m-C_8XQZRUjf3pxmf1zhqHxU6NtuIe_vEBZdAOEsf5g-9W7VEO2BFrM4jSrEqyoJuhlStNpmUTRY6vH1VhHjRC4_f2lzUQIqtVj9Elmk1SCKvQ_3L84iNHOwsG80mToc59vCFcyyJaKTmGEvpj_1IQ-4sXTLAhAEgizH8AxIZRbv7Pk7ztGoRQCUZ9PVnTbvrMHkYUzvxdOmBY4yYquLUXs0eRY2auqcAmtJXbq99tBr4ywDvVDRAHWnprFbLTWJ3JIZDev-fft_viMZGd3F6nvbvKlLcjXNsdNQso72FfFhR9oVnzJaTdfiS9YNZdFHtGq9vS-_Vqxqk5VJFYEWJ2eyjpxwh9xWxX9HXUezJjg6RFcct2lOiKkjIptl9UrWtIP90HNYvLpFUezTIXps0VWf7UR3usi_fyy8rqIowEcx2M65zfs

nucliadb-test:
	nucliadb  --zone europe-1 --maindb test/mainnuclia --blob test/blobnuclia --node test/nodenuclia --log INFO  --key eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6InNhIn0.eyJpc3MiOiJodHRwczovL251Y2xpYS5jbG91ZC8iLCJleHAiOjE2OTcyOTUwNjgsImlhdCI6MTY2NTc1OTA2OCwic3ViIjoiNzIwMGU5ZTYtNGQ3OS00OTc3LWI3MmQtZGQ2Njg1YmZiMWQ3IiwianRpIjoiN2NmZjFmODUtZDhjMy00OGQzLWIzM2YtNTgwNDBmOWZmZGNkIiwia2V5IjoiM2Y3OGUzM2ItNDU0Mi00NWYzLWE2MzctZTZiM2NkN2NmNGY4Iiwia2lkIjoiMWIzZTJhNjQtODJlMS00MWM5LWI1M2ItZWY5NzI0ZTc5NjE4In0.I0kamdtjJkgc8xKFhuFB2I-Uwdh7uJ7MR1aq85vdFX3ll9ewnicAWOwUtsUt37E_juSIWzNrmQq2vlbqqljY-JNO2x4oyqZ1qN-UBYL20nsuI7oqKIZBol_QoKmOUHTCm1ciwNTwckUiudZ3usT2OKNAmEe4pIAQnq57dc_6vj79kG35kb_8J6aqWm0zRj9u_EJCjEB72foK-njjk0QVBDhyTxGbXjdAqdztAq9Ry50ZtkMkgl5_sau5m-C_8XQZRUjf3pxmf1zhqHxU6NtuIe_vEBZdAOEsf5g-9W7VEO2BFrM4jSrEqyoJuhlStNpmUTRY6vH1VhHjRC4_f2lzUQIqtVj9Elmk1SCKvQ_3L84iNHOwsG80mToc59vCFcyyJaKTmGEvpj_1IQ-4sXTLAhAEgizH8AxIZRbv7Pk7ztGoRQCUZ9PVnTbvrMHkYUzvxdOmBY4yYquLUXs0eRY2auqcAmtJXbq99tBr4ywDvVDRAHWnprFbLTWJ3JIZDev-fft_viMZGd3F6nvbvKlLcjXNsdNQso72FfFhR9oVnzJaTdfiS9YNZdFHtGq9vS-_Vqxqk5VJFYEWJ2eyjpxwh9xWxX9HXUezJjg6RFcct2lOiKkjIptl9UrWtIP90HNYvLpFUezTIXps0VWf7UR3usi_fyy8rqIowEcx2M65zfs

nucliadb-oss:
	nucliadb --maindb main --blob blob --node node --log INFO 