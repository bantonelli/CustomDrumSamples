/**
 * Created by brandonantonelli on 1/11/14.
 */
/*
*/

'use strict';
module.exports = function(grunt) {
    grunt.initConfig({
        pkg:grunt.file.readJSON('package.json'),
        // The watch object is specific to the grunt-contrib-watch task
        // This is specified in the task's documentation
        // Paths in the watch object are relative to where the Gruntfile.js is located.
        sass: {                              // Task
            dist: {                            // Target
                options: {                       // Target options
                    style: 'expanded'
                },
                files: {                         // Dictionary of files
                    'cds_components/css/styles.css': 'cds_components/sass/styles.scss'       // 'destination': 'source'
                }
            }
        },
        uglify: {
            my_target: {
                files: {
                    'CustomDrumSamples/static/js/libs/libs.min.js': [
                        'bower_components/classie/classie.js',
                        'bower_components/jquery/dist/jquery.js',
                        'bower_components/jquery.finger/dist/jquery.finger.js',
                        'bower_components/select2/select2.min.js',
                        'bower_components/angular/angular.js',
                        'bower_components/angular-mocks/angular-mocks.js',
                        'bower_components/angular-route/angular-route.js'
                    ],
                    'CustomDrumSamples/static/js/dist/cds.min.js':[
                        'cds_components/js/vendor/detectmobilebrowser',
                        'cds_components/js/vendor/modal-login-nav.js',
                        'cds_components/js/vendor/sidebarEffects.js',
                        'cds_components/js/*.js'
                    ]
                }
            }
        },
        cssmin: {
            target: {
                files: {
                    'CustomDrumSamples/static/css/styles.min.css': [
                        'cds_components/css/select2.css',
                        'cds_components/css/styles.css'
                    ]
                }
            }
        },
        watch: {
            options: {
                livereload: {
                    port: 9090
                }
            },
            // options can also be put inside of a subtask
            // (ie: less can have its own options)
            sass: {
                files:['cds_components/sass/*.scss', 'cds_components/sass/*/*.scss'],
                tasks:['sass']
            },
            html: {
                files:['templates/**/*.html', 'templates/*.html']
            },
            javascript: {
                files:['cds_components/js/*.js', 'cds_components/js/vendor/*.js']
            }

        }
    });
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
};