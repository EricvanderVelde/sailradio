# Sail Radio

This project is about receiving information needed for sailors using a [kiwiSDR](http://kiwisdr.com/) receiver.

The kiwiSDR receiver is capable of receiving multiple signals at the same time.

- NAVTEX
- RTTY
- WeatherFAX (to be added)
- voice broadcasts (to be added)

## Howto
 - install the kiwiclient and fsk decoders
 - update run.sh with the correct directories
 - update the schedule.json with the kiwiSDR host & port
 - update the schedule.json with the transmissions to be received
 - run python cron.py add to add the cron entries (if 'add' is not specified the cron entries will be removed)

### dependencies:
 - [kiwiclient](https://github.com/jks-prv/kiwiclient)
 - [juerec decoders](https://github.com/EricvanderVelde/decoders)
