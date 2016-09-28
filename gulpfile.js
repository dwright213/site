// requirements
var gulp = require('gulp');
var sass = require('gulp-sass');
var postcss = require('gulp-postcss');
var minify = require('gulp-clean-css');
var purify = require('gulp-purifycss');
var sourcemaps = require('gulp-sourcemaps');
var autoprefixer = require('gulp-autoprefixer');
var flexbugs = require('postcss-flexbugs-fixes');

// tasks
gulp.task('styles', function() {
	return gulp.src('static/sass/vendor/bootstrap/bootstrap.scss')
	.pipe(sass())
	.pipe(purify(['./static/js/**/*.js', './templates/*.html']))
	.pipe(postcss([require('postcss-flexbugs-fixes')]))
  	.pipe(autoprefixer({
      browsers: ['last 2 versions'],
      cascade: false
	}))
	.pipe(minify())
  .pipe(gulp.dest('static/css/vendor'))
});

