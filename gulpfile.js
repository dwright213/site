// requirements
var
	gulp = require('gulp'),
	sass = require('gulp-sass'),
	batch = require('gulp-batch'),
	watch = require('gulp-watch'),
	uglify = require('gulp-uglify'),
	concatenate = require('gulp-concat'),
	postcss = require('gulp-postcss'),
	minify = require('gulp-clean-css'),
	purify = require('gulp-purifycss'),
	sourcemaps = require('gulp-sourcemaps'),
	autoprefixer = require('gulp-autoprefixer'),
	flexbugs = require('postcss-flexbugs-fixes'),

	sassets = [
		'static/sass/vendor/bootstrap/bootstrap.scss',
		'static/sass/*.scss'
	];

jsassets = [
	'static/js/vendor/jquery.min.js',
	'static/js/vendor/tether.js',
	'static/js/vendor/bootstrap.js',
	'static/js/vendor/lightbox.js',
	'static/js/*.js'
];

watchDirs = [
	'static/sass/**/*.scss',
	'static/js/vendor/**/*.js',
	'static/js/*.js'
];


// watcher
gulp.task('default', function() {
	watch(watchDirs, batch(function(events, done) {
		gulp.start('styles', done);
		gulp.start('scripts', done);
	}));
});

// tasks
gulp.task('styles', function() {
	return gulp.src(sassets)
		.pipe(sass().on('error', sass.logError))
		// .pipe(purify(['./static/js/vendor/*.js', './static/js/*.js', './templates/*.html']))
		.pipe(postcss([require('postcss-flexbugs-fixes')]))
		.pipe(autoprefixer({
			browsers: ['last 2 versions'],
			cascade: false
		}))
		.pipe(concatenate('styles.css'))
		// .pipe(sourcemaps.init())
		// .pipe(minify())
		// .pipe(sourcemaps.write('maps'))
		.pipe(gulp.dest('static/css'))
});

gulp.task('scripts', function() {
	return gulp.src(jsassets)
		.pipe(concatenate('scripts.js'))
		// .pipe(sourcemaps.init())
		// .pipe(uglify())
		// .pipe(sourcemaps.write('maps'))
		.pipe(gulp.dest('static/js/compiled'))
})
