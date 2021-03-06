# ZStatsPython
Get Player Data From zstats plugin. Not An Official Module.

## Usage
Use the module like this:

```
from zstatspython import zstatspy

db=zstatspy.connect("localhost","root","password", "database")
userstat=zstatspy.getStats("Username",db)
for x in userstat:
    print(x)
```

You can also use it with a UUID. 

```
UUIDstat=zstatspy.getStatsfromUUID("069a79f4-44e9-4726-a5be-fca90e38aaf5",db)
for y in UUIDstat:
    print(y)

```
Sometimes a player might have more than one UUIDs so we recommend using an external username to UUID and then use `getStatsfromUUID` instead of `getStats`

### Functions 
Connect
```
from zstatspython import zstatspy
db=zstatspy.connect("localhost","root","password", "database")
```
GetStats
```
from zstatspython import zstatspy
db=zstatspy.connect("localhost","root","password", "database")
userstat=zstatspy.getStats("Notch",db)
```

GetStatsFromUUID
```
from zstatspython import zstatspy
db=zstatspy.connect("localhost","root","password", "database")
UUIDstat=zstatspy.getStatsfromUUID("19139894-6049-4db7-9c84-da0b99b9ec12",db)
```
GetStat
```
from zstatspython import zstatspy
db=zstatspy.connect("localhost","root","password", "database")
stat=zstatspy.getStat("DEATHS","Notch",db)
```

## Test file
Usage
```
$ python test.py
```
Response:
```
MySQL Login: 
Host: 
```
After Login:
```
Login Succeded
Get Stats
MC Username: 
```
Response After Entering Valid Username
```
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:shovel', 0)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:sword', 877)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:trident', 79)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'DAMAGE_TAKEN', 13823)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:crafted', 1707)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:placed', 9499)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'DEATHS', 22)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'SPRINT_ONE_CM', 1116825)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:afk_time', 0)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:mined', 26969)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:mine_kind', 73)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:craft_kind', 17)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:place_kind', 113)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'PLAY_ONE_MINUTE', 1456104)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:bow', 161)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'MOB_KILLS', 584)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'SLEEP_IN_BED', 8)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:axe', 181)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:pickaxe', 26290)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'ITEM_ENCHANTED', 6)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'CROUCH_ONE_CM', 78580)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:last_played', 1617256053)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'WALK_ONE_CM', 1734979)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'DAMAGE_DEALT', 81056)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'TALKED_TO_VILLAGER', 159)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:hoe', 22)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'TRADED_WITH_VILLAGER', 50)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'BOAT_ONE_CM', 1498835)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:mob_kind', 25)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'CHEST_OPENED', 195)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'AVIATE_ONE_CM', 2187704)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'FISH_CAUGHT', 5)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:slain_kind', 4)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'RECORD_PLAYED', 3)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'ARMOR_CLEANED', 0)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'NOTEBLOCK_PLAYED', 0)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'BELL_RING', 98)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:craft_0001_GOLD_INGOT', 949)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:craft_0002_GREEN_DYE', 286)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:craft_0003_GOLD_BLOCK', 256)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:place_0001_WHITE_WOOL', 1282)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:place_0002_FISHING_ROD', 639)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:place_0003_EMERALD_BLOCK', 575)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:mine_0001_STONE', 17735)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:mine_0002_DIAMOND_ORE', 3001)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:mine_0003_NETHERRACK', 1253)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:mob_0001_SKELETON', 220)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:mob_0002_ZOMBIE', 178)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:mob_0003_CREEPER', 30)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:slain_0001_SKELETON', 1)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:slain_0002_VINDICATOR', 1)
('19139894-6049-4db7-9c84-da0b99b9ec12', 'z:slain_0003_PLAYER', 1)
```
## License
This software is licensed under the MIT license. Feel free to use it however you like.
