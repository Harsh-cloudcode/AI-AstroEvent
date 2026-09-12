import astronomy

print("Astronomy Engine test")

# UTC time: 2026-09-10 14:30 UTC
time = astronomy.Time.Make(
    2026,
    9,
    10,
    14,
    30,
    0
)

observer = astronomy.Observer(
    18.5204,
    73.8567,
    0
)

print("Time created")

equator = astronomy.Equator(
    astronomy.Body.Jupiter,
    time,
    observer,
    True,
    True
)

print("Equator:")
print("RA:", equator.ra)
print("DEC:", equator.dec)
print("Distance:", equator.dist)

horizon = astronomy.Horizon(
    time,
    observer,
    equator.ra,
    equator.dec,
    astronomy.Refraction.Airless
)

print("Horizon:")
print("Altitude:", horizon.altitude)
print("Azimuth:", horizon.azimuth)