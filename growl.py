from nose.plugins import Plugin
import gntp.notifier


class NoseGrowl(Plugin):
    name = 'growl'

    def finalize(self, result=None):
        growl = gntp.notifier.GrowlNotifier(notifications=["Tests Ran"])
        growl.register()

        if result.wasSuccessful():
            title = "Tests Passed"
        else:
            title = "Tests Failed"
            
        message = "{} Tests\n{} Skipped\n{} Failures\n{} Errors".format(
            result.testsRun,
            len(result.skipped),
            len(result.failures),
            len(result.errors),
        )

        growl.notify(
            noteType="Tests Ran",
            title=title,
            description=message,
            sticky=False,
            priority=1,
        )
