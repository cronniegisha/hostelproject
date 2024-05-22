from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Room
from .serializers import RoomSerializer

class RoomAPITests(APITestCase):

    def setUp(self):
        # Create initial test data
        self.room1 = Room.objects.create(name='Room 101', capacity=10, floor=1, is_reserved=True, reserved_for='John Doe')
        self.room2 = Room.objects.create(name='Room 102', capacity=20, floor=2, is_reserved=False, reserved_for=None)
        self.valid_room_data = {'name': 'Room 103', 'capacity': 15, 'floor': 1, 'is_reserved': True, 'reserved_for': 'Jane Doe'}
        self.invalid_room_data = {'name': '', 'capacity': -5, 'floor': -1, 'is_reserved': False, 'reserved_for': ''}


    def test_create_valid_room(self):
        # Test creating a room with valid data
        response = self.client.post(reverse('room-list-create'), self.valid_room_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Room.objects.count(), 3)
        new_room = Room.objects.get(name='Room 103')
        self.assertEqual(new_room.capacity, 15)
        self.assertEqual(new_room.floor, 1)
        self.assertTrue(new_room.is_reserved)
        self.assertEqual(new_room.reserved_for, 'Jane Doe')

    def test_create_invalid_room(self):
        # Test creating a room with invalid data
        response = self.client.post(reverse('room-list-create'), self.invalid_room_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Room.objects.count(), 2)

    def test_update_room(self):
        # Test updating a room
        update_data = {'name': 'Room 101 Updated', 'capacity': 12, 'floor': 1, 'is_reserved': False, 'reserved_for': ''}
        response = self.client.put(reverse('room-update', kwargs={'pk': self.room1.pk}), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.room1.refresh_from_db()
        self.assertEqual(self.room1.name, 'Room 101 Updated')
        self.assertEqual(self.room1.capacity, 12)
        self.assertEqual(self.room1.floor, 1)
        self.assertFalse(self.room1.is_reserved)
        self.assertEqual(self.room1.reserved_for, '')

   