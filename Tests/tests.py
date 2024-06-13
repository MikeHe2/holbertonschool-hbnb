#!/usr/bin/python3
import unittest
from datetime import datetime
from Model.basemodel import BaseModel
from Model.place import Place
from Model.users import Users
from Model.reviews import Reviews

"""
This imports unittest  providing the TestCase class and testing utilities,
datetime providing classes for manipulating dates and times
basemodel the BaseModel class from the Model package
place the Place class from the Model package
users the Users class from the Model package
reviews the Reviews class from the Model package

"""


class TestModel(unittest.TestCase):
    """Test suite for the Model module."""

    # Consistency check test
    def test_consistency_checks(self):
        """Test consistency checks."""
        Users.users = []
        updated_at = datetime.now()
        created_at = datetime.now()
        user = Users(id=1, updated_at=updated_at, created_at=created_at,
                     host_id="Owner", place_id="Owned place",
                     review="Great place to stay!",
                     email="user@email.com",
                     first_name="Nelly", last_name="Sierra")
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    # Relationship integrity
    def test_relationship_integrity(self):
        """Test relationship integrity."""
        Users.users = []
        updated_at = datetime.now()
        created_at = datetime.now()
        user = Users(id=1, created_at=created_at, updated_at=updated_at,
                     host_id="Owner", place_id="Owned place",
                     review="Great place to stay!", email="user@email.com",
                     first_name="Michael",
                     last_name="Hernandez")
        place = Place(id=1, created_at=created_at, updated_at=updated_at,
                      name="Place Test", description="Test description",
                      address="420 Test street",
                      latitude=48.8584, longitude=2.3370, host=user,
                      price_per_night=100, max_guests=6)
        review = Reviews(id=1, created_at=created_at, updated_at=updated_at,
                         place=place,
                         rating=5, comment="Amazing experience!")
        self.assertEqual(place.host, user)
        self.assertEqual(review.place, place)

    # Business rules application
    def test_business_rule_enforcement(self):
        """Test business rule enforcement."""
        updated_at = datetime.now()
        created_at = datetime.now()
        user1 = Users(id=1, updated_at=updated_at, created_at=created_at,
                      host_id="Owner", place_id="Owned place",
                      review="Great place to stay!", email="user@email.com",
                      first_name="Saul",
                      last_name="Vera")
        with self.assertRaises(ValueError):
            user2 = Users(id=2, created_at=created_at, updated_at=updated_at,
                          host_id="Owner", place_id="Owned place",
                          review="Great place to stay!",
                          email=user1.email,
                          first_name="Jesse", last_name="Pinkman")

        # Test user uniqueness
        with self.assertRaises(ValueError):
            user3 = Users(id=3, created_at=created_at, updated_at=updated_at,
                          host_id="Owner", place_id="Owned place",
                          review="Great place to stay!",
                          email=user1.email,
                          first_name="Mike",
                          last_name="Ehrmantraut")

    # User creation validation
    def test_user_creation_validation(self):
        """Test user creation validation."""
        created_at = datetime.now
        updated_at = datetime.now()
        with self.assertRaises(ValueError):
            user = Users(id=1, created_at=created_at, updated_at=updated_at,
                         host_id="Owner", place_id="Owned place",
                         review="Great place to stay!",
                         email="invalid_email",
                         first_name="Lalo",
                         last_name="Salamanca")

    # Unique email constraint
    def test_unique_email_constraint(self):
        """Test unique email constraint."""
        Users.users = []
        updated_at = datetime.now()
        created_at = datetime.now()
        user1 = Users(id=1, updated_at=updated_at, created_at=created_at,
                      host_id="Owner", place_id="Owned place",
                      review="Great place to stay!",
                      email="user@email.com",
                      first_name="Kim",
                      last_name="Wexler")
        print("User 1 created with email:", user1.email)
        print("Existing users:", [user.email for user in Users.users])
        try:
            user2 = Users(id=2, created_at=created_at, updated_at=updated_at,
                          host_id="Owner", place_id="Owned place",
                          review="Great place to stay!",
                          email=user1.email,
                          first_name="Hank",
                          last_name="Schrader")
        except ValueError as e:
            print("Caught ValueError:", e)
        else:
            self.fail("Expected ValueError not raised")

    # Update mechanism
    def test_update_mechanism(self):
        """Test update mechanism."""
        Users.users = []
        created_at = datetime.now()
        updated_at = datetime.now()
        user = Users(id=1, created_at=created_at, updated_at=updated_at,
                     host_id="Owner", place_id="Owned place",
                     review="Great place to stay!",
                     email="user@email.com",
                     first_name="Nacho",
                     last_name="Varga")
        user.first_name = "Nacho"
        self.assertEqual(user.first_name, "Nacho")

    # Place instantiation
    def test_place_instantiation(self):
        """Test place instantiation."""
        updated_at = datetime.now()
        created_at = datetime.now()
        place = Place(id=1, created_at=created_at, updated_at=updated_at,
                      name="Place test", description="Test description",
                      address="420 Test street",
                      latitude=48.8584, longitude=2.3370, host=None,
                      price_per_night=100, max_guests=6)
        self.assertEqual(place.name, "Place test")

    def test_host_assignment_rules(self):
        """Test host assignment rules."""
        updated_at = datetime.now()
        created_at = datetime.now()
        user1 = Users(id=1, created_at=created_at, updated_at=updated_at,
                      host_id="Owner", place_id="Owned place",
                      review="Great place to stay!",
                      email="user#1@email.com",
                      first_name="Gus",
                      last_name="Fring")
        user2 = Users(id=2, created_at=created_at, updated_at=updated_at,
                      host_id="Owner", place_id="Owned place",
                      review="Great place to stay!",
                      email="user#2@email.com",
                      first_name="Chuck",
                      last_name="McGill")
        place = Place(id=1, created_at=created_at, updated_at=updated_at,
                      name="Place test",
                      description="Test description",
                      address="420 Test street",
                      latitude=48.8584, longitude=2.3370, host=user1,
                      price_per_night=100, max_guests=6)
        # Test that assigning a new host to a place that already
        # has one raises ValueError
        with self.assertRaises(ValueError):
            place.new_host(user2)

    # Place attribute validation
    def test_place_attribute_validation(self):
        """Test place attribute validation."""
        updated_at = datetime.now()
        created_at = datetime.now()
        place = Place(id=1, created_at=created_at, updated_at=updated_at,
                      name="Place test", description="Test description",
                      address="420 Test street", latitude=48.8584,
                      longitude=2.3370, host=None, price_per_night=100,
                      max_guests=6)
        self.assertEqual(place.latitude, 48.8584)
        self.assertEqual(place.longitude, 2.3370)
        self.assertEqual(place.price_per_night, 100)
        self.assertEqual(place.max_guests, 6)

    # Deleting places
    def test_deleting_places(self):
        """Test deleting places."""
        Users.users = []
        updated_at = datetime.now()
        created_at = datetime.now()
        user = Users(id=1, created_at=created_at, updated_at=updated_at,
                     host_id="Owner", place_id="Owned place",
                     review="Great place to stay!",
                     email="user@email.com",
                     first_name="Jimmy",
                     last_name="McGill")
        place = Place(id=1, created_at=created_at, updated_at=updated_at,
                      name="Place test",
                      description="Test description",
                      address="420 Test street",
                      latitude=48.8584, longitude=2.3370, host=user,
                      price_per_night=100, max_guests=6)
        place.delete()
        self.assertIsNone(place.host)

    # Amenity addition
    def test_amenity_addition(self):
        """Test amenity addition."""
        created_at = datetime.now()
        updated_at = datetime.now()
        place = Place(id=1, created_at=created_at, updated_at=updated_at,
                      name="Place test",
                      description="Test description",
                      address="420 Test street",
                      latitude=48.8584, longitude=2.3370,
                      host=None, price_per_night=100, max_guests=6)
        place.add_amenity("Wi-Fi")
        place.add_amenity("Pool")
        self.assertCountEqual(place.amenities, ["Wi-Fi", "Pool"])

    # Retrieve and update amenities
    def test_retrieve_and_update_amenities(self):
        """Test retrieve and update amenities."""
        updated_at = datetime.now()
        created_at = datetime.now()
        place = Place(id=1, created_at=created_at, updated_at=updated_at,
                      name="Place test", description="Test description",
                      address="420 Test street",
                      latitude=48.8584, longitude=2.3370, host=None,
                      price_per_night=100, max_guests=6)
        place.add_amenity("Wi-Fi")
        place.update_amenity("Wi-Fi", "High-speed Wi-Fi")
        self.assertIn("High-speed Wi-Fi", place.amenities)

    def test_not_own_review(self):
        """Test that a place owner cannot review their own place."""
        # Create a user who is also a host
        updated_at = datetime.now()
        created_at = datetime.now()
        host_id = 1
        place_id = 1
        host = Users(id=host_id, created_at=created_at, updated_at=updated_at,
                     host_id="Owner", place_id="Owned place",
                     review="Great place to stay!", email="owner@email.com",
                     first_name="Host", last_name="Owner")
        place = Place(id=place_id, created_at=created_at,
                      updated_at=updated_at,
                      name="Place test", description="Test description",
                      address="420 Test street",
                      latitude=48.8584, longitude=2.3370, price_per_night=100,
                      max_guests=6, host=host)

        # Attempt to review own place
        review_text = "Great place to stay!"
        with self.assertRaises(ValueError):
            host.not_own_review(host_id, place_id, review_text)


if __name__ == '__main__':
    unittest.main()
