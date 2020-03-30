# Project: Discord Bot
-[] For users to earn 2 XP points everytime they particpate in the chat.
- So, for every text that is sent is 2 XP points. 
- Everytime you level up, it gets harder and harder for you to level up again. 
- The chat telling you what level and XP you hva everytime you level up.

- A leaderboard that includes the top level users.
- A automatic(scheduled) leaderboard every week so annouce the top players.
- The ability to check you level.


### Planning:

- [ ] Decide what actions earn xp (time spent, participation in chat, etc.)
- [ ] Read up on data persistence in Python
- [ ] Choose plain text (JSON) or Postgres database and create the appropriate file(s)
- [ ] Update README.md with more specific information about the bot's operation
- [ ] Set up a Discord server for testing
- [ ] Create an application with a bot on the Discord Developer portal

### Execution:

- [ ] Verify the bot can get onto your test server
- [ ] Write a listener that checks the database when someone logs in. If the user exists in the database, start tracking xp. If not, add t the user and then start tracking xp
- [ ] Write a command that displays the top 5 users with the highest cumulative xp
- [ ] Write a command that displays the top 5 users with the highest xp for the *current week*
