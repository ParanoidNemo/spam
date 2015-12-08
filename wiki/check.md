check - Global check types
=====

The check module supplies a bounch of functions usefull to check if the interested resources is present on the system.

check.**prog(prg)** - Check if an executable exists in /usr/bin. Return Bool values.

check.**date(timestamp)** - Compare the date into the timestamp file with the actual one and return the difference between the two.

check.**distro** - Return the distro you are on due to the package manager in use.