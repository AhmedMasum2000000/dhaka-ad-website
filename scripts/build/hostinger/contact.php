<?php
// POST-only callback form -> email. No credentials stored here.
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); exit; }
if (!function_exists('mb_substr')) { function mb_substr($s, $a, $l = null) { return substr($s, $a, $l); } }
$thanks = function () { header('Location: /thank-you/'); exit; };
$fail = function ($code, $text) { http_response_code($code); header('Content-Type: text/html; charset=UTF-8');
  exit('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Dhaka AD</title><body style="font:18px/1.5 system-ui,sans-serif;padding:32px;max-width:560px"><p>' . $text . '</p><p><a href="/contact/">Back to the form</a> or call <a href="tel:+8801840860284">+880 1840 860 284</a>.</p>'); };
if (!empty($_POST['website'])) $thanks();
$ts = (int)($_POST['ts'] ?? 0);
if ($ts && (time() - $ts < 3 || time() - $ts > 86400)) $thanks();
$priv = dirname($_SERVER['DOCUMENT_ROOT']);
$rl = $priv . '/form-rate'; @mkdir($rl, 0700);
$rf = $rl . '/' . md5($_SERVER['REMOTE_ADDR'] ?? '');
$hits = array_filter(explode(',', (string)@file_get_contents($rf)), function ($t) { return $t !== '' && (int)$t > time() - 600; });
if (count($hits) >= 5) $fail(429, 'Too many requests. Please call us instead.');
$hits[] = time(); @file_put_contents($rf, implode(',', $hits), LOCK_EX);
$clean = function ($k, $max) { $v = trim((string)($_POST[$k] ?? '')); $v = str_replace(["\r", "\n"], ' ', $v); return mb_substr(strip_tags($v), 0, $max); };
$name = $clean('name', 80); $phone = $clean('phone', 30); $area = $clean('area', 60); $brand = $clean('brand', 60);
$msg = mb_substr(strip_tags((string)($_POST['message'] ?? '')), 0, 2000);
if (substr_count(strtolower($msg . $name . $brand), 'http') > 2) $thanks();
$phone = strtr($phone, ['০'=>'0','১'=>'1','২'=>'2','৩'=>'3','৪'=>'4','৫'=>'5','৬'=>'6','৭'=>'7','৮'=>'8','৯'=>'9']);
$digits = preg_replace('/[^0-9+]/', '', $phone);
if ($name === '' || !preg_match('/^\+?[0-9]{6,15}$/', $digits)) $fail(400, 'Please add your name and a phone number.');
$body = "Callback request\nName: $name\nPhone: $phone\nBrand: $brand\nArea: $area\n\n$msg\n";
$hdr = "From: Dhaka AD Website <info@dhakaad.com>\r\nReply-To: info@dhakaad.com\r\nMIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit";
$ok = mail('info@dhakaad.com', '=?UTF-8?B?' . base64_encode('Callback request from dhakaad.com: ' . $name) . '?=', $body, $hdr, '-finfo@dhakaad.com');
if (!$ok) {
  @file_put_contents($priv . '/form-fallback.log', date('c') . ' ' . json_encode([$name, $phone, $brand, $area, $msg], JSON_UNESCAPED_UNICODE) . "\n", FILE_APPEND | LOCK_EX);
  $fail(503, 'Sorry, the form could not send just now.');
}
$thanks();
