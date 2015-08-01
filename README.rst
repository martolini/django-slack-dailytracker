=====
Daily tracker
=====

Simple integration for slack and django to track daily progress and sync with the team.

-----------
Quick start
-----------

1. Add "dailytracker" to your INSTALLED_APPS

2. Include the dailytrackers URLconf in your project urls.py like this::

    url(r'^dailytracker/', include('polls.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Create an incoming webhook for your slackteam and name the bot whatever you want, create a team in the admin panel and put the url from the webhook into webhook_url on your team.

5. Create a slack command (I use /dailyupdate) and point it to http://yourdomain.com/dailytracker/ or whatever you chose as the url.

6. Create cronjobs with the commands `python manage.py request_daily_update`, `python manage.py daily_update_dunning`, and `python manage.py daily_update_summary`.

7. Let your team simply write /dailyupdate Finished the login flow on the iOS application - and the bot will update everyone through daily_update_summary.
