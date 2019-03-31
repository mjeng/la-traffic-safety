app:
	sleep 4 && open http://localhost:5000/ &
	export GOOGLE_APPLICATION_CREDENTIALS=/Users/owner/eecs/personal-projects/active_/lahacks/la-traffic-safety/lahacks19-2678365782f8.json && ./temp.sh && python main.py
	

deploy:
	echo y | gcloud app deploy && gcloud app browse