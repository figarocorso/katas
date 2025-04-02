# BUDAPEST HOTEL

## About this kata

Welcome to the Grand Budapest Hotel. Our friend Gustave needs to adapt his belove hotel to the new times, for that he is asking us to help him with room bookings. Surely it is a great idea, but funny that his is trusting us for this important task.

Because we have read couple of books we want to create a client side process and a server checking room availability. The first one will handle the interaction with the user, meanwhile the latest one will take over the responsability of knowing which rooms are available for book. For now it is not fully clear why we are dividing this kata into two efforts, but looks like a nice idea if we need to divide our efforts into two groups.

## Client side kata

### Retrieve the list of available rooms
* Create a program that prints the list of available rooms (our server side service is returning a unordered array/list) in a comma-separated format:
```
$ list
101, 102, 301
```
* Now we want the output to be ordered and separated by room floor (the last two digits are the number of the room at that floow, meanwhile hundreds and thousands digit (and others at its left) is the floor where the room is located
```
$ list
101, 102, 105
201, 202
503, 510
1001
```

### Book a room
* This is great. Time for bookings. The user should be able to introduce the number of the room to book, and we should be able to ask our server side service for that reservation (server side service is answering with a boolean if the booking was succesful or not)
```
$ book 101
Your booking is confirmed
```
* If there was a problem during the booking process we should show an error message and list available rooms
```
$ book 101
Sorry, there was a problem during the booking. These are the rooms currently available:
102, 105
201, 202
503, 510
1001
```

### Book a room for a selected time range
* It is time for introduccing dates for the booking:
  * Dates should be in the future
  * It is mandatory that there are two dates
  * First date should be earlier than the second date
  * The date format should always be YYYY-MM-DD
```
$ list 2030-01-01 2030-01-03
102, 105
201, 202
503, 510
1001
$ book 102 2030-01-01 2030-01-03
Your booking is confirmed
```

### Clever bookings
* We have discovered people just want a room for a time range. Let's do that. Client should ask the server for the available rooms and create a booking for a room following these constraints:
  * We cannot book 10th floor suites
  * If possible we don't book 1st floor rooms
  * For the rest of the floors we try to fill the hotel getting paired occupation for every floor (when in tie, let's fill the hotel from botton to top)
```
$ book 2030-01-01 2030-01-03
# Internally we run "book 201 2030-01-01 2030-01-03"
Your booking is confirmed
```
* We have discovered that this aproach is costing us a lot in getting cleaning service from one room to a different one. Let's fill the hotel from bottom to top.
```
$ book 2030-01-01 2030-01-03
# Internally we run "book 102 2030-01-01 2030-01-03"
Your booking is confirmed
```
* It looks we are not that clever anymore. What a surprise! Let's just random book a room so hotel keeps balanced.

## Server side kata

### Retrieve the list of available rooms
* First task is simply enough to return the list of available rooms
```
list()
[101, 102, 301]
```

### Book a room
* From the list of avilable rooms we need to remove those that have been booked. For that, we need to support the ability to book a room. We need to return a boolean depending if the booking was successful or not on our end
  * Book number should be an integer
```
list()
[101, 102, 301]
book(101)
true
list()
[102, 301]
book(101)
false
```

### Book a room for a selected time range
* Every backend service loves dealing with dates and timezones, let's introduce the concept of booking a room for a specific time
  * The list of available rooms now will depend on the dates queried
  * The booking now has to have a initial date and and end date for each room reservation
  * We cannot book a room in the past
  * Initial date should be earlier than end date
  * We cannot book a room that has colliding date ranges
  * But we can book a room with two bookings, the first finishing on the day the second booking starts
```
list("2030-01-01", "2030-01-03")
[101, 102, 301]
book(101, "2030-01-01", "2030-01-03")
true
```

### Block rooms with maintenance works
* Sometimes a room has no booking, but we cannot list that room as available

### Bussiness metrics
The more we understand users, the best service we can provide, let's support two queries:
* Return all the bookings starting between two dates
* Return all the bookings starting between two dates, including how many days in advance the booking was made
* Date rages should honor same limitations as before
```
list_bookings("2025-01-01", "2025-12-31")
[{"room": 101, "start_date": "2025-01-06", "end_date": "2025-01-07", "days_from_booking": 86}, ...]
```