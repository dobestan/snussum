module.exports = (grunt) ->
    grunt.initConfig
        clean: [
            'components'
            'static'
        ]

        bowercopy:
            options:
                clean: true
            libs:
                options:
                    destPrefix: 'snussum/components'

        shell:
            pep8:
                command: 'pep8'

            unittest:
                command: 'NOSE_NOCAPTURE=1 python snussum/manage.py test snussum/ --verbosity=2 --noinput'

        watch:
            jshint:
                files: '<%= jshint.files %>'
                tasks: 'jshint'

            django:
                files: '**/*.py'
                tasks: 'test'

        notify:
            pep8:
                options:
                    title: "PEP8 - Success!"
                    message: "A Foolish Consistency is the Hobgoblin of Little Minds"

            unittest:
                options:
                    title: "UnitTest - Suceess!"
                    message: "Keep Calm and Love TDD"


    grunt.loadNpmTasks 'grunt-contrib-clean'
    grunt.loadNpmTasks 'grunt-bowercopy'
    grunt.loadNpmTasks 'grunt-shell'
    grunt.loadNpmTasks 'grunt-contrib-watch'
    grunt.loadNpmTasks 'grunt-notify'


    grunt.registerTask 'test', [
        'shell:pep8'
        'notify:pep8'
        'shell:unittest'
        'notify:unittest'
    ]


    grunt.registerTask 'default', [
        'clean'
        'bowercopy'
        'watch'
    ]
