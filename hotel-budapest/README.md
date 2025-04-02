# BUDAPEST HOTEL

## About this kata

Welcome to the Grand Budapest Hotel. Our friend Gustave needs to adapt his belove hotel to the new times, for that he is asking us to help him with room bookings. Surely it is a great idea, but funny that his is trusting us for this important task.

Because we have read couple of books we want to create a client side process and a server checking room availability. The first one will handle the interaction with the user, meanwhile the latest one will take over the responsability of knowing which rooms are available for book. For now it is not fully clear why we are dividing this kata into two efforts, but looks like a nice idea if we need to divide our efforts into two groups.

## Client side kata

### Problem description

#### Retrieve the list of available rooms
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
* It is time for introduccing dates for the booking:
  * Dates should be in the future
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