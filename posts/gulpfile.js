var gulp = require('gulp');
var less = require('gulp-less');

gulp.task('less', function() {
  return gulp.src('static/less/style.less')
  .pipe(less())
  .pipe(gulp.dest('static/css/'));
});

gulp.task('watch', function() {
  gulp.watch('static/less/style.less', ['less']);
})
