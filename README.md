# Project: Discord Bot



Make commits to save levels like google docs save work.
To track player's points on discord.
Make a leaderboard to see who is the highest in the class.

### Planning:
-[ ] Decide what actions earn xp (time spent, participation in chat, etc.)
-[ ] Read up on data persistence in Python
-[ ] Choose plain text (JSON) or Postgres database and create the appropriate file(s)
-[ ] Update README.md with more specific information about the bot's operation
-[ ] Set up a Discord server for testing
-[ ] Create an application with a bot on the Discord Developer portal

### Execution:
-[ ] Verify the bot can get onto your test server
-[ ] Write a listener that checks the database when someone logs in. If the user exists in the database, start tracking xp. If not, add the user and then start tracking xp
-[ ] Write a command that displays the top 5 users with the highest cumulative xp
-[ ] Write a command that displays the top 5 users with the highest xp for the *current week*
