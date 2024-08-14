SecuritySystem
---

Intro
---
Inspired by youtuber Tech with Tim, i am mirroring his security system project.


Camera service
---
Here we will make the service that take the feed from a camera and detects if an intruder is present.
Will use face recognition to make that determination.
Framework in use:
FastAPI
OpenCV

Will use message broker RabbitMQ, to notify backend that a video is ready to be pulled and that it can be collected through an API or database, have not determined how yet.

Backend
---

Dashboard
---

Notification Service
---

