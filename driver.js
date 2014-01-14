var system = require('system');
var args = system.args;

var page = require("webpage").create();

page.onConsoleMessage = function(msg) {
    system.stderr.writeLine('CONSOLE: ' + msg);
};

page.open(args[1], function() {
    page.includeJs('http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js',
                   function () {
                       var content = page.evaluate(function () {
                           $('script').remove();
                           return $('html')[0].outerHTML;
                       });
                       system.stdout.writeLine(content);
                       phantom.exit(0);
                   });
});
