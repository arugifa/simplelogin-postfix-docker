# Docker Image for SimpleLogin Postfix

No Postfix image, tailor-made for SimpleLogin, currently exists.

Let's fix that, by providing something very simple, which just accepts a volume
to be mount on `/etc/postfix`, in order to load Postfix configuration files.
