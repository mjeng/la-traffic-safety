app:
	export GOOGLE_APPLICATION_CREDENTIALS=$(pwd)/lahacks19-2678365782f8.json
	sleep 4 && open http://localhost:5000/ &
	python3 app.py

deploy:
	echo y | gcloud app deploy && gcloud app browse