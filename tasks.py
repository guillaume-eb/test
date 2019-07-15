from invoke_release.tasks import *  # noqa: F403


# See documentation at https://github.com/eventbrite/invoke-release for help using this and releasing services
configure_release_parameters(  # noqa: F405
    module_name='test',
    display_name='Test Guillaume',
    use_pull_request=True,
    use_tag=False
)