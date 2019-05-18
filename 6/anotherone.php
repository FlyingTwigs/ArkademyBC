<?php
require_once('./main/query.php')
$query = new DBquery();

if ($_GET['action']=="users")
{
    print_r($query->getUsers());
}
elseif($_GET['action']="addUsers")
{
    if(isset($_POST['add']) == "add")
    {
        if($_POST['addusers'])
        {
            if($query->addUsers($_POST['addusers']))
            {
                foreach($query->getUsers() as $row):
                    echo $query->addUserSkillsId($row['id']);
                    echo "Berhasil ditambahkan <a href='/index.php'> Ke halaman utama </a>";
                    exit();
                endforeach;
            }
        } else {
            echo "Silakan masukkan nama <a href='/index.php'>";
        }
    } else {
        header('Location: index.php');
        exit();
    }
}
elseif($_GET['action'] == "update")
{
    if(isset($_POST['update']) == "add");
    {
        if($_POST['id'] && $_POST['skill'])
        {
            $query->updateUserSkills($_POST['skill'], $_POST['id']);
            header("Location: /index.php");
        }
    }
}
