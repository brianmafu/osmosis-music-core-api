-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 23, 2019 at 03:01 PM
-- Server version: 10.3.16-MariaDB
-- PHP Version: 7.1.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `client_demo_musicplayer_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--


--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `admin_name`, `admin_email`, `admin_username`, `admin_password`, `status`, `created_date`) VALUES
(1, 'admin', 'admin@admin.com', 'admin', '21232f297a57a5a743894a0e4a801fc3', 'ENABLE', '2019-10-22 14:52:38');

-- --------------------------------------------------------

--
-- Table structure for table `ads_settings`
--


--
-- Dumping data for table `ads_settings`
--

INSERT INTO `ads_settings` (`ads_id`, `ads_title`, `ads_id_value`, `ads_status`, `last_updated`) VALUES
(1, 'Banner', '', 'ENABLE', '2019-10-16 22:37:32'),
(2, 'Interstital', '', 'ENABLE', '2019-10-16 22:37:32'),
(3, 'Native', '', 'ENABLE', '2019-10-16 22:37:32');

-- --------------------------------------------------------

--
-- Table structure for table `album`
--


--
-- Dumping data for table `album`
--

INSERT INTO `album` (`album_id`, `artist_id`, `album_name`, `album_image`, `album_status`, `created_date`) VALUES
(1, '1', '7/27', '7-27.jpg', 'ENABLE', '2019-09-24 02:14:50');

-- --------------------------------------------------------

--
-- Table structure for table `api_list`
--



--
-- Dumping data for table `api_list`
--

INSERT INTO `api_list` (`api_id`, `api_name`, `api_link`, `api_type`, `created_date`) VALUES
(1, 'Register ', 'API/register', 'POST', '2019-08-06 05:05:38'),
(3, 'Get All Settings Flag', 'API/register', 'POST', '2019-08-06 05:05:38'),
(2, 'Login', 'API/login', 'POST', '2019-08-06 05:05:38'),

(4, 'Home Component List', 'API/getCategory', 'POST', '2019-08-06 05:05:38'),
(5, 'Home', 'API/home', 'POST', '2019-08-06 05:05:38'),
(6, 'View Single Music Screen', 'API/playMusic', 'POST', '2019-08-06 05:05:38'),
(7, 'View Single Artist Screen', 'API/viewArtist', 'POST', '2019-08-06 05:05:38'),
(8, 'View Single Movie Screen', 'API/viewMovie', 'POST', '2019-08-06 05:05:38'),
(9, 'View Single Album Screen', 'API/viewAlbum', 'POST', '2019-08-06 05:05:38'),
(10, 'Like', 'API/like', 'POST', '2019-08-06 05:05:38'),
(11, 'Unlike', 'API/unlike', 'POST', '2019-08-06 05:05:38'),
(12, 'Create new playlist ', 'API/createPlayList', 'POST', '2019-08-06 05:05:38'),
(13, 'Add In Playlist', 'API/addInPlaylist', 'POST', '2019-08-06 05:05:38'),
(14, 'Remove From Playlist', 'API/removeFromPlaylist', 'POST', '2019-08-06 05:05:38'),
(15, 'Get User\'s Playlists ', 'API/getPlaylists', 'POST', '2019-08-06 05:05:38'),
(16, 'Get user playlist\'s music', 'API/getPlaylistMusic', 'POST', '2019-08-06 05:05:38'),
(17, 'Delete Playlist', 'API/deletePlayList', 'POST', '2019-08-06 05:05:38'),
(18, 'Get All Categories', 'API/getAllCategories', 'POST', '2019-08-06 05:05:38'),
(19, 'Get music by category', 'API/getCategoryMusic', 'POST', '2019-08-06 05:05:38'),
(20, 'Get Packages', 'API/getPackages', 'POST', '2019-08-06 05:05:38'),
(21, 'Search', 'API/search', 'POST', '2019-08-06 05:05:38'),
(22, 'Get All Musics', 'API/getAllMusics', 'POST', '2019-08-06 05:05:38'),
(23, 'Get All Artists', 'API/getAllArtists', 'POST', '2019-08-06 05:05:38'),
(24, 'Get All Albums', 'API/getAllAlbums', 'POST', '2019-08-06 05:05:38'),
(25, 'Get All Movies', 'API/getAllMovies', 'POST', '2019-08-06 05:05:38'),
(26, 'Get Payment Methods', 'API/getPaymentMethods', 'POST', '2019-08-06 05:05:38'),
(27, 'Get Stripe Payment Webview', 'API/getStripePaymentScreen', 'POST', '2019-08-06 05:05:38'),
(28, 'Get User Package Info ', 'API/getUserPackageInfo', 'POST', '2019-08-06 05:05:38'),
(29, 'Check If Downloads allowed', 'API/isAllowDownloads', 'POST', '2019-08-06 05:05:38'),
(30, 'Edit Profile', 'API/ediProfile', 'POST', '2019-08-06 05:05:38');

-- --------------------------------------------------------

--
-- Table structure for table `api_list_parameters`
--


--
-- Dumping data for table `api_list_parameters`
--

INSERT INTO `api_list_parameters` (`api_list_parameters_id`, `api_list_id`, `api_list_parameters_name`) VALUES
(1, 1, 'user_email'),
(2, 1, 'user_password'),
(3, 1, 'user_token'),
(4, 1, 'user_profile_pic'),
(5, 2, 'user_email'),
(6, 2, 'user_password'),
(7, 2, 'user_token  '),
(8, 5, 'home_components_name'),
(9, 5, 'user_id'),
(10, 5, 'is_myProfile'),
(11, 5, 'start (optional)'),
(12, 5, 'end (optional)'),
(13, 6, 'music_id'),
(14, 6, 'user_id'),
(15, 7, 'user_id'),
(16, 7, 'artist_id'),
(17, 8, 'movie_id'),
(18, 8, 'user_id'),
(19, 9, 'album_id'),
(20, 9, 'user_id'),
(21, 10, 'user_id'),
(22, 10, 'like_type'),
(23, 10, 'like_type_id'),
(24, 11, 'user_id'),
(25, 11, 'like_type'),
(26, 11, 'like_type_id'),
(27, 12, 'user_id'),
(28, 12, 'user_playlist_name'),
(29, 13, 'user_id'),
(30, 13, 'user_playlist_id'),
(31, 13, 'music_id'),
(32, 14, 'user_id'),
(33, 14, 'music_id'),
(34, 15, 'user_id'),
(35, 16, 'user_id'),
(36, 16, 'user_playlist_id'),
(37, 17, 'user_id'),
(38, 17, 'user_playlist_id'),
(39, 18, 'user_id'),
(40, 19, 'user_id'),
(41, 19, 'category_id'),
(42, 21, 'search'),
(43, 22, 'user_id'),
(44, 22, 'start'),
(45, 22, 'end'),
(46, 23, 'user_id'),
(47, 23, 'start'),
(48, 23, 'end'),
(49, 24, 'user_id'),
(50, 24, 'start'),
(51, 24, 'end'),
(52, 25, 'user_id'),
(53, 25, 'start'),
(54, 25, 'end'),
(55, 27, 'user_id'),
(56, 27, 'package_id'),
(57, 27, 'total_package_price'),
(58, 28, 'user_id'),
(59, 29, 'user_id'),
(60, 30, 'user_id'),
(61, 30, 'user_name'),
(62, 30, 'user_profile_pic');

-- --------------------------------------------------------

--
-- Table structure for table `artist`
--



--
-- Dumping data for table `artist`
--

INSERT INTO `artist` (`artist_id`, `artist_name`, `artist_image`, `artist_status`, `created_date`) VALUES
(1, 'Fifth Harmony', 'FifthHarmony.jpg', 'ENABLE', '2019-09-24 02:13:38');

-- --------------------------------------------------------

--
-- Table structure for table `banner_slider`
--


--
-- Dumping data for table `banner_slider`
--

INSERT INTO `banner_slider` (`banner_slider_id`, `banner_slider_name`, `banner_slider_name_alignment`, `banner_slider_image`, `banner_slider_show_button`, `banner_slider_button_alignment`, `banner_slider_button_text`, `banner_slider_order`, `banner_slider_status`, `created_date`) VALUES
(1, 'Bollywood Cinema', 'Left', 'bollywood_cinema.jpg', 0, 'Left', '', 1, 'ENABLE', '2019-09-23 05:30:23');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--



--
-- Dumping data for table `category`
--

INSERT INTO `category` (`category_id`, `category_name`, `parent_category_id`, `category_status`, `created_date`) VALUES
(1, 'Pop', 0, 'ENABLE', '2019-09-24 00:04:31');

-- --------------------------------------------------------

--
-- Table structure for table `home_components`
--


--
-- Dumping data for table `home_components`
--

INSERT INTO `home_components` (`home_components_id`, `home_components_name`, `home_components_description`, `home_components_item_display_count`, `home_components_order`, `home_components_status`, `created_date`) VALUES
(1, 'Banner Slider', 'This banner slider would be displayed on top of home page.', 4, 1, 'ENABLE', '2019-09-22 23:34:14'),
(2, 'Most Played', 'Most Played music', 6, 2, 'ENABLE', '2019-09-22 23:50:41'),
(3, 'Popular Albums', 'Popular Albums (most visited)', 6, 3, 'ENABLE', '2019-09-22 23:51:37'),
(4, 'Favourite Artists', 'Favourite Artists (most favourite)', 6, 4, 'ENABLE', '2019-09-22 23:53:09'),
(6, 'Recommended Music', 'Recommended Music (most favourite)', 6, 6, 'ENABLE', '2019-09-22 23:54:47'),
(7, 'Recommended Album', 'Recommended Album (most favourite)', 6, 6, 'ENABLE', '2019-09-22 23:54:47'),
(10, 'Categories', 'Category List', 8, 10, 'DISABLE', '2019-09-23 02:48:35'),
(8, 'Recommended Movies', 'Recommended Movies (most favourite)', 6, 6, 'ENABLE', '2019-09-22 23:54:47'),
(9, 'Popular Movies', 'Popular Movies (most visited)', 6, 7, 'ENABLE', '2019-09-22 23:51:37'),
(5, 'Recently Played', 'Recently Played ', 6, 5, 'ENABLE', '2019-09-22 23:53:09');

-- --------------------------------------------------------

--
-- Table structure for table `liked`
--


--
-- Dumping data for table `liked`
--

INSERT INTO `liked` (`like_id`, `user_id`, `like_type`, `like_type_id`, `like_date`, `created_date`) VALUES
(1, 1, 'Music', 2, '2019-10-22', '2019-10-22 19:29:56'),
(2, 1, 'Music', 1, '2019-10-17', '2019-10-17 18:06:45'),
(3, 1, 'Artist', 1, '2019-09-27', '2019-09-27 18:20:53'),
(4, 1, 'Album', 1, '2019-09-30', '2019-09-30 11:41:30'),
(5, 1, 'Movie', 1, '2019-10-23', '2019-10-23 11:11:38');

-- --------------------------------------------------------

--
-- Table structure for table `movie`
--



--
-- Dumping data for table `movie`
--

INSERT INTO `movie` (`movie_id`, `movie_name`, `movie_description`, `movie_image`, `movie_year`, `movie_status`, `created_date`) VALUES
(1, 'Aquaman', 'Aquaman - 2019', 'Aquaman.jpg', '2019', 'ENABLE', '2019-09-25 22:20:47');

-- --------------------------------------------------------

--
-- Table structure for table `music`
--



--
-- Dumping data for table `music`
--

INSERT INTO `music` (`music_id`, `music_title`, `music_file`, `music_image`, `category_id`, `album_id`, `artist_id`, `movie_id`, `music_size`, `music_duration`, `music_status`, `created_date`) VALUES
(1, 'Work from Home', 'FifthHarmony-WorkfromHomeftTyDol.mp3', '7-27.jpg', 3, 1, '1', NULL, NULL, '3:40', 'ENABLE', '2019-09-24 23:11:40'),
(2, 'The Life', 'FifthHarmony-TheLife.mp3', '7-27.jpg', 3, 1, '1', NULL, NULL, '3:20', 'ENABLE', '2019-09-24 23:11:40'),
(3, 'Thats My Girl', 'FifthHarmony-ThatsMyGirl.mp3', '7-27.jpg', 3, 1, '1', NULL, NULL, '3:54', 'ENABLE', '2019-09-24 23:11:40'),
(4, 'The Legend of Atlan', 'Aquaman-TheLegendofAtlan.mp3', 'aquaman.jpg', 0, 0, '0', 1, NULL, '2:07', 'ENABLE', '2019-09-24 23:11:40');

-- --------------------------------------------------------

--
-- Table structure for table `notification_settings`
--


--
-- Dumping data for table `notification_settings`
--

INSERT INTO `notification_settings` (`notification_id`, `settings_name`, `settings_value`, `settings_status`, `last_updated`) VALUES
(1, 'API Key', '', 'ENABLE', '2019-07-11 03:05:25'),
(2, 'Sender Id', '', 'ENABLE', '2019-07-11 03:05:25');

-- --------------------------------------------------------

--
-- Table structure for table `package_settings`
--


--
-- Dumping data for table `package_settings`
--

INSERT INTO `package_settings` (`package_id`, `package_name`, `package_duration`, `package_price`, `package_status`, `package_note`, `created_date`) VALUES
(1, 'Free', '-', '0', 'ENABLE', 'This is free package.', '2019-09-09 02:31:38'),
(2, '12 Months', '12', '59.99', 'ENABLE', 'This is 1 Month package with 9.99/month and total payment is 9.99.', '2019-09-13 00:41:00');

-- --------------------------------------------------------

--
-- Table structure for table `payment_method`
--


--
-- Dumping data for table `payment_method`
--

INSERT INTO `payment_method` (`payment_method_id`, `payment_method_name`, `payment_method_currency`, `payment_method_public_key`, `payment_method_secret_key`, `payment_method_status`, `created_date`) VALUES
(1, 'Stripe', 'USD', '', '', 'ENABLE', '2019-10-21 01:26:08');

-- --------------------------------------------------------

--
-- Table structure for table `recently_view`
--



--
-- Dumping data for table `recently_view`
--

INSERT INTO `recently_view` (`recently_view_id`, `recently_view_type`, `recently_view_type_id`, `user_id`, `created_date`) VALUES
(1, 'Music', 1, 1, '2019-09-26 16:26:49'),
(2, 'Music', 2, 1, '2019-09-26 16:27:07'),
(3, 'Music', 3, 1, '2019-09-26 16:27:43'),
(4, 'Music', 4, 2, '2019-09-26 16:45:10'),
(5, 'Album', 1, 1, '2019-09-27 12:57:59'),
(6, 'Movie', 1, 1, '2019-10-17 11:39:30'),
(7, 'Artist', 1, 1, '2019-10-17 16:50:05');

-- --------------------------------------------------------

--
-- Table structure for table `settings_flag`
--



--
-- Dumping data for table `settings_flag`
--

INSERT INTO `settings_flag` (`settings_flag_id`, `settings_flag_name`, `settings_flag_value`, `created_date`) VALUES
(1, 'Notification', 'ENABLE', '2019-09-24 22:40:02'),
(2, 'Package', 'ENABLE', '2019-09-24 22:40:02'),
(3, 'Ads', 'ENABLE', '2019-09-24 22:40:02');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `user_name`, `user_email`, `user_password`, `user_phone`, `user_profile_pic`, `user_package_id`, `user_package_paid_date`, `user_package_expiry_date`, `user_token`, `created_date`) VALUES
(1, 'Test', 'testuser@test.test', NULL, NULL, 'user_1_2019-09-23-11-16-39.jpg', 1, NULL, '2020-01-21 05:37:13', '', '2019-09-19 08:40:52');

-- --------------------------------------------------------

--
-- Table structure for table `user_payment`
--


-- --------------------------------------------------------

--
-- Table structure for table `user_playlist`
--


--
-- Dumping data for table `user_playlist`
--

INSERT INTO `user_playlist` (`user_playlist_id`, `user_id`, `user_playlist_name`, `created_date`) VALUES
(1, 1, 'My Favourite', '2019-10-01 12:13:35');

-- --------------------------------------------------------

--
-- Table structure for table `user_playlist_music`
--


--
-- Dumping data for table `user_playlist_music`
--

INSERT INTO `user_playlist_music` (`user_playlist_music_id`, `user_playlist_id`, `user_id`, `music_id`, `created_date`) VALUES
(1, 1, 1, 1, '2019-10-01 13:44:47'),
(2, 1, 1, 3, '2019-10-02 10:35:53');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `ads_settings`
--
ALTER TABLE `ads_settings`
  ADD PRIMARY KEY (`ads_id`);

--
-- Indexes for table `album`
--
ALTER TABLE `album`
  ADD PRIMARY KEY (`album_id`);

--
-- Indexes for table `api_list`
--
ALTER TABLE `api_list`
  ADD PRIMARY KEY (`api_id`);

--
-- Indexes for table `api_list_parameters`
--
ALTER TABLE `api_list_parameters`
  ADD PRIMARY KEY (`api_list_parameters_id`);

--
-- Indexes for table `artist`
--
ALTER TABLE `artist`
  ADD PRIMARY KEY (`artist_id`);

--
-- Indexes for table `banner_slider`
--
ALTER TABLE `banner_slider`
  ADD PRIMARY KEY (`banner_slider_id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `home_components`
--
ALTER TABLE `home_components`
  ADD PRIMARY KEY (`home_components_id`);

--
-- Indexes for table `liked`
--
ALTER TABLE `liked`
  ADD PRIMARY KEY (`like_id`);

--
-- Indexes for table `movie`
--
ALTER TABLE `movie`
  ADD PRIMARY KEY (`movie_id`);

--
-- Indexes for table `music`
--
ALTER TABLE `music`
  ADD PRIMARY KEY (`music_id`);

--
-- Indexes for table `notification_settings`
--
ALTER TABLE `notification_settings`
  ADD PRIMARY KEY (`notification_id`);

--
-- Indexes for table `package_settings`
--
ALTER TABLE `package_settings`
  ADD PRIMARY KEY (`package_id`);

--
-- Indexes for table `payment_method`
--
ALTER TABLE `payment_method`
  ADD PRIMARY KEY (`payment_method_id`);

--
-- Indexes for table `recently_view`
--
ALTER TABLE `recently_view`
  ADD PRIMARY KEY (`recently_view_id`);

--
-- Indexes for table `settings_flag`
--
ALTER TABLE `settings_flag`
  ADD PRIMARY KEY (`settings_flag_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `user_payment`
--
ALTER TABLE `user_payment`
  ADD PRIMARY KEY (`user_payment_id`);

--
-- Indexes for table `user_playlist`
--
ALTER TABLE `user_playlist`
  ADD PRIMARY KEY (`user_playlist_id`);

--
-- Indexes for table `user_playlist_music`
--
ALTER TABLE `user_playlist_music`
  ADD PRIMARY KEY (`user_playlist_music_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `ads_settings`
--
ALTER TABLE `ads_settings`
  MODIFY `ads_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `album`
--
ALTER TABLE `album`
  MODIFY `album_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `api_list`
--
ALTER TABLE `api_list`
  MODIFY `api_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `api_list_parameters`
--
ALTER TABLE `api_list_parameters`
  MODIFY `api_list_parameters_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT for table `artist`
--
ALTER TABLE `artist`
  MODIFY `artist_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `banner_slider`
--
ALTER TABLE `banner_slider`
  MODIFY `banner_slider_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `home_components`
--
ALTER TABLE `home_components`
  MODIFY `home_components_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `liked`
--
ALTER TABLE `liked`
  MODIFY `like_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `movie`
--
ALTER TABLE `movie`
  MODIFY `movie_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `music`
--
ALTER TABLE `music`
  MODIFY `music_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `notification_settings`
--
ALTER TABLE `notification_settings`
  MODIFY `notification_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `package_settings`
--
ALTER TABLE `package_settings`
  MODIFY `package_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `payment_method`
--
ALTER TABLE `payment_method`
  MODIFY `payment_method_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `recently_view`
--
ALTER TABLE `recently_view`
  MODIFY `recently_view_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `settings_flag`
--
ALTER TABLE `settings_flag`
  MODIFY `settings_flag_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `user_payment`
--
ALTER TABLE `user_payment`
  MODIFY `user_payment_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_playlist`
--
ALTER TABLE `user_playlist`
  MODIFY `user_playlist_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `user_playlist_music`
--
ALTER TABLE `user_playlist_music`
  MODIFY `user_playlist_music_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;