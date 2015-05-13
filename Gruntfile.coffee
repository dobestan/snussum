module.exports = (grunt) ->
  grunt.initConfig
      clean: [
        'snussum/snussum/components'
      ]

      bowercopy:
        options:
          clean: true
        libs:
          options:
            destPrefix: 'snussum/snussum/components'
          files:
            'js/jquery.min.js': 'jquery/dist/jquery.min.js'
            'js/jquery.min.map': 'jquery/dist/jquery.min.map'
            'js/jquery-cookie.js': 'jquery-cookie/jquery.cookie.js'
            'js/bootstrap.min.js': 'bootstrap/dist/js/bootstrap.min.js'
            'js/bootstrap-notify.min.js': 'remarkable-bootstrap-notify/bootstrap-notify.min.js'
            'js/bootstrap-switch.min.js': 'bootstrap-switch/dist/js/bootstrap-switch.min.js'
            'js/bootstrap-datetimepicker.min.js': 'eonasdan-bootstrap-datetimepicker/build/js/bootstrap-datetimepicker.min.js'
            'js/moment.min.js': 'moment/min/moment.min.js'
            'js/bootstrap-tagsinput.min.js': 'bootstrap-tagsinput/dist/bootstrap-tagsinput.min.js'
            'js/highcharts.min.js': 'highcharts/highcharts.js'

            'sass/bourbon/': 'bourbon/app/assets/stylesheets'

            'css/bootstrap.min.css': 'bootstrap/dist/css/bootstrap.min.css'
            'css/animate.min.css': 'animate.css/animate.min.css'
            'css/font-awesome.min.css': 'fontawesome/css/font-awesome.min.css'
            'css/bootstrap-switch.min.css': 'bootstrap-switch/dist/css/bootstrap3/bootstrap-switch.min.css'
            'css/bootstrap-datetimepicker.min.css': 'eonasdan-bootstrap-datetimepicker/build/css/bootstrap-datetimepicker.min.css'
            'css/bootstrap-tagsinput.css': 'bootstrap-tagsinput/dist/bootstrap-tagsinput.css'

            'fonts/': ['NanumBarunGothic/', 'fontawesome/fonts/']


      sass:
        dist:
          files:
            'snussum/snussum/static/css/application.css': 'snussum/snussum/static/sass/application.scss'

          options:
            loadPath: [
              'snussum/snussum/components/sass/bourbon/'
            ]

      jshint:
        files: 'snussum/snussum/static/js/**/*.js'

      cssmin:
        target:
          files:
            'snussum/snussum/static/deploy/css/snussum.min.css': [
              'snussum/snussum/static/css/application.css'
            ]

      uglify:
        target:
          files:
            'snussum/snussum/static/deploy/js/snussum.min.js': [
              'snussum/snussum/components/js/jquery.min.js'
            ]

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
  grunt.loadNpmTasks 'grunt-contrib-cssmin'
  grunt.loadNpmTasks 'grunt-contrib-uglify'


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

  grunt.registerTask 'deploy-staticfiles', [
    'bowercopy'
    'sass'
    'cssmin'
    'uglify'
  ]

  grunt.registerTask 'default', [
    'clean'
    'bowercopy'
    'sass-with-notify'
    'jshint-with-notify'
    'watch'
  ]
