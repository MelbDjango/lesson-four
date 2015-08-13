## TODO

- Highlight the need to redirect after successful object creation. Stops the ability to perform some types of replay attacks.
- Discuss django.shortcuts.redirect (and how that plays with URL reversing)
- (Maybe) adding a class to the form field if there is an error


## Fixed

- Add redirects to all `POST` blocks
- `stop` and `end` were being used in different places and caused the end date to not save properly
