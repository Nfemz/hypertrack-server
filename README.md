# Server for HyperTrack Webhook Implementation

## StudentTrack

Welcome to StudentTrack, your one stop shop for all highschool student location services. With StudentTrack, you'll never lose a student again.

Tired of losing Seniors during lunch? Too many Senior skip days? Sign out and sign in too manual? Look no further.

StudentTrack will:

Be required in order to use mobile data or wifi on a cellular device on school grounds
Report on student location within campus during the configurable time and date period
Alert administrative staff if a student leaves campus without permission
Report out student traffic throughout campus allowing you to optimize scheduling for minimal traffic

## API Reference

Fetch api documentation as JSON object:
```
curl -X GET https://https://hypertrack-server.herokuapp.com/
```

Fetch all devices:
```
curl -x GET https://https://hypertrack-server.herokuapp.com/devices
```

Fetch a specific device:
```
curl -x GET https://https://hypertrack-server.herokuapp.com/device/{device_id}
```

Fetch location history for a device:
```
curl -x GET https://https://hypertrack-server.herokuapp.com/locations/{device_id}
````

Update a device document:
```
curl -x POST https://https://hypertrack-server.herokuapp.com/device/{device_id}
--data-raw '{
  <optional> "device_status": "{device_status}",
  <optional> "device_user": "{device_user}"
}
```

Webhook for HyperTrack device data:
```
curl -x POST https://https://hypertrack-server.herokuapp.com/
```
