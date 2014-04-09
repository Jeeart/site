module.exports = function(grunt) {

    grunt.initConfig({
        // concat: {
        //     options: {
        //         separator: ';'
        //     },
        //     basic: {
        //         src: [
        //             'wrestle/lib/quintus.js',
        //             'wrestle/lib/quintus_2d.js',
        //             'wrestle/lib/quintus_anim.js',
        //             'wrestle/lib/quintus_audio.js',
        //             'wrestle/lib/quintus_input.js',
        //             'wrestle/lib/quintus_scenes.js',
        //             'wrestle/lib/quintus_sprites.js',
        //             'wrestle/lib/quintus_touch.js',
        //             'wrestle/lib/quintus_ui.js',

        //             'wrestle/js/cons.js',
        //             'wrestle/js/player.js',
        //             'wrestle/js/boss.js',
        //             'wrestle/js/cd.js',
        //             'wrestle/js/io.js',
        //             'wrestle/js/scaffold.js',
        //             'wrestle/js/wrestle.js'
        //         ],
        //         dest: 'wrestle/wrestle.js'
        //     }
        // },
        // uglify: {
        //     options: {
        //         mangle: false
        //     },
        //     my_target: {
        //         files: {
        //             'wrestle/wrestle.min.js': [
        //                 'wrestle/wrestle.js'
        //             ]
        //         }
        //     },
        //     all: {
        //         files: {
        //             'build/js/all.min.js': ['build/js/all.js']
        //         }
        //     }
        // },
        // copy: {
        //     main: {
        //         files: [
        //           // includes files within path
        //           //{expand: true, src: ['path/*'], dest: 'dest/', filter: 'isFile'},

        //           // includes files within path and its sub-directories
        //           {expand: true, src: ['images/**', 'css/**', 'js/**', 'game/**'], dest: 'build/'},

        //           // makes all src relative to cwd
        //           //{expand: true, cwd: 'path/', src: ['**'], dest: 'dest/'},

        //           // flattens results to a single level
        //           //{expand: true, flatten: true, src: ['path/**'], dest: 'dest/', filter: 'isFile'}
        //         ]
        //       }
        // },
        less: {
            production: {
                options: {
                  paths: ["css"],
                  cleancss: true
                },
                files: {
                  "django_app/jeeart/static_media/css/page_home.css": "django_app/jeeart/static_media/less/page_home.less",
                  "django_app/jeeart/static_media/css/page_blog.css": "django_app/jeeart/static_media/less/page_blog.less",
                  "django_app/jeeart/static_media/css/page_dispic.css": "django_app/jeeart/static_media/less/page_dispic.less"
                }
              }
        },
        watch: {
            less: {
                files: ['django_app/jeeart/static_media/less/*.less'],
                tasks: ['less']
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('default', ['less', 'watch']);

}