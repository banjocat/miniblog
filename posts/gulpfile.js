var gulp = require('gulp');
var less = require('gulp-less');
var rename = require('gulp-rename');

var FILES = {
  'js': [
    './node_modules/jquery/dist/jquery.min.js',
    './node_modules/markdown/lib/markdown.js'
  ]
}
gulp.task('less', function() {
  return gulp.src('static/less/style.less')
  .pipe(less())
  .pipe(gulp.dest('static/css/'));
});

gulp.task('watch', function() {
  gulp.watch('static/less/style.less', ['less']);
})

gulp.task('js', function() {
  return gulp.src(FILES.js)
  .pipe(rename({dirname: ''}))
  .pipe(gulp.dest('static/js/'));
})
