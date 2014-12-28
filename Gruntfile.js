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
                    'CustomDrumSamples/static/css/styles.css': 'CustomDrumSamples/static/sass/styles.scss'       // 'destination': 'source'
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
                files:['CustomDrumSamples/static/sass/*.scss', 'CustomDrumSamples/static/sass/*/*.scss'],
                tasks:['sass']
            },
            html: {
                files:['templates/**/*.html', 'templates/*.html']
            },
            javascript: {
                files:['CustomDrumSamples/static/js/*.js', 'CustomDrumSamples/static/js/vendor/*.js']
            }
        }
    });
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
};