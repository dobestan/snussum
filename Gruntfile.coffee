module.exports = (grunt) ->
  grunt.initConfig
      clean: [
        'snussum/components'
      ]

      bowercopy:
        options:
          clean: true
        libs:
          options:
            destPrefix: 'snussum/components'
          files:
            'sass/bourbon/': 'bourbon/app/assets/stylesheets'
            'sass/neat/': 'neat/app/assets/stylesheets'

      sass:
        dist:
          files:
            'snussum/snussum/static/css/application.css': 'snussum/snussum/static/sass/application.scss'

          options:
            loadPath: [
              'snussum/components/sass/bourbon/'
              'snussum/components/sass/neat/'
            ]

      jshint:
        files: 'snussum/snussum/**/*.js'

      shell:
        pep8:
          command: 'pep8'

        unittest:
          command: 'NOSE_NOCAPTURE=1 python snussum/manage.py test snussum/ --verbosity=2 --noinput'

      watch:
        jshint:
          files: '<%= jshint.files %>'
          tasks: 'jshint-with-notify'

        django:
          files: '**/*.py'
          tasks: 'test'

        sass:
          files: '**/*.scss'
          tasks: 'sass-with-notify'

      notify:
        pep8:
          options:
            title: "PEP8 - Success!"
            message: "A Foolish Consistency is the Hobgoblin of Little Minds"

        unittest:
          options:
            title: "UnitTest - Suceess!"
            message: "Keep Calm and Love TDD"

        sass:
          options:
            title: "SASS - Success!"
            message: "Syntactically Awesome Style Sheets"

        jshint:
          options:
            title: "jshint - Success!"
            message: "JavaScript Code Quality Tool"


  grunt.loadNpmTasks 'grunt-contrib-clean'
  grunt.loadNpmTasks 'grunt-bowercopy'
  grunt.loadNpmTasks 'grunt-contrib-sass'
  grunt.loadNpmTasks 'grunt-shell'
  grunt.loadNpmTasks 'grunt-contrib-watch'
  grunt.loadNpmTasks 'grunt-notify'
  grunt.loadNpmTasks 'grunt-contrib-jshint'


  grunt.registerTask 'test', [
    'shell:pep8'
    'notify:pep8'
    'shell:unittest'
    'notify:unittest'
  ]

  grunt.registerTask 'sass-with-notify', [
    'sass'
    'notify:sass'
  ]

  grunt.registerTask 'jshint-with-notify', [
    'jshint'
    'notify:jshint'
  ]

  grunt.registerTask 'default', [
    'clean'
    'bowercopy'
    'sass-with-notify'
    'jshint-with-notify'
    'watch'
  ]
