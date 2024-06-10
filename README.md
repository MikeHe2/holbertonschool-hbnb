<<<<<<< HEAD
# HbnB Evolution Project
## Model + API

![gif](https://developers.giphy.com/branch/master/static/api-512d36c09662682717108a38bbb5c57d.gif)

## <u> What’s Cooking in Part 1? </u>
1. `Sketching with UML:` You’ll kick things off by drawing out the backbone of our application using UML (Unified Modeling Language). Think of it like creating the architectural blueprint for a building. It’s where you decide how your classes and components will interact.

2. `Testing Our Logic:` After setting up our blueprint, it’s time to make sure everything works as planned. You’ll create tests for the API and business logic. It’s like making sure all the gears turn smoothly in a machine.

3. `Building the API:` Now, for the real deal - implementing the API. This is where your blueprint comes to life. You’ll use Flask to create an API that plays well with our business logic and file-based persistence (for now).

4. `File-Based Data Storage:` We’re starting simple with a file-based system for storing our data. Choose your format – text, JSON, XML – you name it. Keep in mind that we’ll shift to a database later, so build it smart!

5. `Packaging with Docker:`Finally, you’ll wrap everything up in a neat Docker image. It’s like packing your app in a container that can be easily moved and deployed anywhere.

## <u> The Three Layers of Our API Cake:</u>

* `Services Layer:` This is where our API greets the world. It handles all the requests and responses.

* `Business Logic Layer:` The brain of the operation. This is where all the processing and decision-making happens.

* `Persistence Layer:` For now, it’s our humble file system, but we’ll graduate to a database in the future.


## <u> The Data Model: Key Entities</u>
1. `Places:` These are the heart of our app. Each place (like a house, apartment, or room) has characteristics like name, description, address, city, latitude, longitude, host, number of rooms, bathrooms, price per night, max guests, amenities, and reviews.

2. `Users:` Users are either owners (hosts) or reviewers (commenters) of places. They have attributes like email, password, first name, and last name. A user can be a host for multiple places and can also write reviews for places they don’t own.

3. `Reviews:` Represent user feedback and ratings for a place. This is where users share their experiences.

4. `Amenities:` These are features of places, like Wi-Fi, pools, etc. Users can pick from a catalog or add new ones.

5. `Country and City:` Every place is tied to a city, and each city belongs to a country. This is important for categorizing and searching places.

### <u>Business Logic: Rules to Live By</u>
`Unique Users:` Each user is unique and identified by their email.

`One Host per Place:` Every place must have exactly one host.

`Flexible Hosting:` A user can host multiple places or none at all.

`Open Reviewing:` Users can write reviews for places they don’t own.

`Amenity Options:` Places can have multiple amenities from a catalog, and users can add new ones.

`City-Country Structure:` A place belongs to a city, cities belong to countries, and a country can have multiple cities.

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _  

**As you design and implement these features, remember that our application will grow. The choices you make now should allow for easy additions and changes later, especially when we switch from file-based to database storage.**

 **In our pursuit of creating a robust and efficient application, it’s crucial that every entity in our data model, except for Country includes the following attributes.:**

`Unique ID (UUID4):` Every object - whether it’s a Place, User, Review, Amenity or City - must have a unique identifier. This ID should be generated using UUID4 to ensure global uniqueness. This is critical for identifying and managing entities across our application consistently.

`Creation Date` (<span style="color:red;">created_at</span>): This attribute will record the date and time when an object is created. It’s vital for tracking the lifespan of our data and understanding the usage patterns.

`Update Date` (<span style="color:red;">updated_at</span>): Similarly, each object should have an attribute to record the last update made. This helps in maintaining the historical accuracy of our data and is essential for any modifications or audit trails.

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
#### <u>Why These Attributes Matter?</u>

* **Uniqueness:** The UUID4 ensures that each entity is distinct, eliminating any confusion or overlap, especially crucial when we scale up.

* **Traceability:** With <span style="color:red;">created_at</span> and <span style="color:red;">updated_at</span>, we can track the lifecycle of each entity, which is invaluable for debugging, auditing, and understanding user interactions over time.

* When designing your classes and database schemas (in the later stages), make sure these attributes are included as a standard part of every entity.

* Utilize Python’s uuid module to generate UUID4 ids.

* Leverage Python’s datetime module to record timestamps for creation and updates.    

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _  

# TASKS

### `0. UML Design`
Objectives

* **Develop a Comprehensive UML Diagram:** Your UML diagram should include all the entities discussed (Places, Users, Reviews, Amenities, Country, City) and their relationships.

* **Consider Future Extensions:** While focusing on the current requirements, design your UML with potential future expansions in mind (like adding more entities or relationships). 1ay to visualize a system’s architectural blueprints, including elements like activities, components, and interactions.

* **<span style="color:red;">UML Class Diagram Tutorial:</span>** For this task, focus on Class Diagrams, which represent the static structure of a system by showing system classes, their attributes, methods, and the relationships between the classes.

### `1. Classes and Business Logic Implementation`
Objectives

1. **Implement the Classes:** Develop the classes as per your UML diagram, ensuring each class has the necessary attributes and methods.

2. **Apply Business Logic:** Implement the business rules that were outlined, such as unique user identification, one host per place, and review systems.

3. **Test Functionality:** Write unit tests to verify that your classes and business logic are working as expected.

### `2. Persistence Implementation`
Objectives

* Develop an interface-based persistence layer that supports easy modification and extension.

* Implement a unified DataManager class that adheres to the defined interface, capable of handling CRUD operations across different entity types.

* Maintain flexibility to transition between different storage mechanisms in the future, such as file-based storage and databases.

### `3. Implement the User Management Endpoints`
Objectives

* Implement endpoints for creating, retrieving, updating, and deleting users.

* Ensure that each endpoint correctly processes requests and returns the appropriate responses in a consistent format.

* Validate inputs to prevent incorrect data from being accepted by the API.

### `4. Implement the Country and City Management Endpoints`
Objectives

* Develop endpoints to retrieve pre-loaded country data and manage city entities.

* Ensure accurate linkage between cities and their respective countries.

* Implement endpoints that allow for the addition, retrieval, update, and deletion of city data.

### `5. Implement the Amenity Management Endpoints`
Objectives

* Develop endpoints for creating, retrieving, updating, and deleting amenity entities.

* Ensure data integrity and consistency for amenities that can be linked to multiple places.

### `6. Implement the Places Management Endpoints`
Objectives

* Develop endpoints for creating, retrieving, updating, and deleting place entities.

* Ensure each place is correctly linked to an existing city and can associate with amenities as specified.

* Provide detailed and structured output formats for API responses.

### `7. Implement the Review Management Endpoints`
Objectives

* Develop endpoints for managing reviews, ensuring they are properly linked to both users and places.

* Enforce business rules and data integrity in review management.

* Provide detailed API responses for better integration and debugging.

### `8. Containerize the Application`
## **Objectives**

**Create a Dockerfile:** Define the process for building your Flask application into a Docker container using Alpine Linux and configuring it with Gunicorn.

**Manage Application Port via Environment Variables:** Enable configuration of the application’s port through environment variables for flexibility.

**Implement Data Persistence:** Set up a Docker volume to persist application data, ensuring data is maintained across container restarts.

## **Requirements**

**Dockerfile:** Create a Dockerfile that details the environment setup, including application dependencies and server configurations.

**Environment Variables:** Use environment variables to manage configurations like the application port.

**Persistent Volume:** Configure a Docker volume that will be used to store and persist application data.
=======
# holbertonschool-hbnb
>>>>>>> ca98cf5d141522e4e2f0e499833a36c0dd35f0a9
